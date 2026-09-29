#!/usr/bin/env python3
"""Check (or update) imagery requirements in source/_data/models.json.

The source of truth is the platform configs in the awesome-configs repo:
``configs/default`` and ``configs/customer``. Each model in models.json names
its config folder in ``requirements.config``; this script reads that config's
requirements (``requirements_file`` from inference.yml, or requirements.yml
next to it) and compares them with the catalog.

    python3 sync_model_requirements.py                       # report drift, exit 1 if any
    python3 sync_model_requirements.py --write               # update "requirements" lines
    python3 sync_model_requirements.py --configs ../awesome-configs

Only the ``requirements`` line of each model is rewritten. The text shown on
the pages (``zoom``, ``best_with``, ``specs.resolution``) stays hand-written;
the Sphinx build warns when it no longer matches ``requirements``.
Scenario requirements come from block descriptions and are not checked here.

Needs PyYAML (pip install pyyaml).
"""
import argparse
import json
import os
import re
import sys

import yaml

CATALOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source", "_data", "models.json")


def read_requirements(configs_root, config):
    folder = os.path.join(configs_root, "configs", config)
    inference = os.path.join(folder, "inference.yml")
    path = os.path.join(folder, "requirements.yml")
    if os.path.exists(inference):
        with open(inference, encoding="utf-8") as fh:
            meta = yaml.safe_load(fh) or {}
        if meta.get("requirements_file"):
            path = os.path.normpath(os.path.join(folder, meta["requirements_file"]))
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    sources = data.get("sources", data)
    tiles = sources.get("xyz") or sources.get("tms") or {}
    local = sources.get("local") or {}

    def pair(section, lo, hi):
        if section.get(lo) is None or section.get(hi) is None:
            return None
        return [section[lo], section[hi]]

    rec_tiles, req_tiles = tiles.get("recommended") or {}, tiles.get("required") or {}
    rec_local, req_local = local.get("recommended") or {}, local.get("required") or {}
    out = {"recommended": {}, "required": {}}
    if pair(rec_tiles, "min_zoom", "max_zoom"):
        out["recommended"]["zoom"] = pair(rec_tiles, "min_zoom", "max_zoom")
    if pair(rec_local, "min_res", "max_res"):
        out["recommended"]["gsd"] = pair(rec_local, "min_res", "max_res")
    if req_tiles.get("min_zoom") is not None:
        out["required"]["min_zoom"] = req_tiles["min_zoom"]
    if pair(req_local, "min_res", "max_res"):
        out["required"]["gsd"] = pair(req_local, "min_res", "max_res")
    return out, os.path.relpath(path, configs_root)


def model_block(text, model_id):
    start = text.index('"id": "%s"' % model_id, text.index('"models"'))
    end = text.index("\n    }", start)
    return start, end


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--configs", default=os.path.join(here, "..", "awesome-configs"),
                        help="path to the awesome-configs repo (default: ../awesome-configs)")
    parser.add_argument("--write", action="store_true", help="update models.json")
    args = parser.parse_args()

    with open(CATALOG, encoding="utf-8") as fh:
        text = fh.read()
    catalog = json.loads(text)
    drift = 0
    for model in catalog["models"]:
        current = model.get("requirements") or {}
        config = current.get("config")
        if not config:
            print("skip  %-22s no config in default/customer" % model["id"])
            continue
        try:
            found, source = read_requirements(args.configs, config)
        except FileNotFoundError as exc:
            print("ERROR %-22s %s" % (model["id"], exc))
            drift += 1
            continue
        mine = {k: current.get(k, {}) for k in ("recommended", "required")}
        if mine == found:
            print("ok    %-22s %s" % (model["id"], source))
            continue
        drift += 1
        print("DRIFT %-22s %s\n      catalog: %s\n      config:  %s" % (
            model["id"], source, json.dumps(mine), json.dumps(found)))
        if args.write:
            new = dict(current, **found)
            new = {k: new[k] for k in ("config", "recommended", "required", "note") if k in new}
            start, end = model_block(text, model["id"])
            block = text[start:end]
            block = re.sub(r'"requirements": \{.*\}(,?)\n',
                           lambda m: '"requirements": %s%s\n' % (json.dumps(new, ensure_ascii=False), m.group(1)),
                           block, count=1)
            text = text[:start] + block + text[end:]

    if args.write and drift:
        json.loads(text)
        with open(CATALOG, "w", encoding="utf-8") as fh:
            fh.write(text)
        print("\nUpdated %s. Now update zoom, best_with and specs.resolution of the changed models "
              "and rebuild; the build warns where page text and requirements disagree." % CATALOG)
    return 1 if drift and not args.write else 0


if __name__ == "__main__":
    sys.exit(main())
