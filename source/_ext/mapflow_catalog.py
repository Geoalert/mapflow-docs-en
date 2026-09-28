"""Mapflow model catalog -> Sphinx components.

One JSON file, ``source/_data/models.json``, describes every AI model and
scenario. The same file is published with each HTML build as ``/models.json``
so the website, Mapflow Web and the QGIS plugin can show the same cards,
prices and copy.

The directives below turn catalog entries into reStructuredText and parse it
in place. Nothing is emitted as raw HTML, so:

* every sentence ends up in the page's gettext catalog and can be translated
  in ``locale/<lang>/LC_MESSAGES/userguides/*.po`` like hand-written text;
* links are real Sphinx cross-references (checked at build time, correct in
  every language build);
* the output degrades to plain paragraphs in non-HTML builders.

Directives
----------
``.. mf-model-gallery::``      grid of model cards  (``:availability: default|custom``)
``.. mf-workflow-gallery::``   grid of "bring your own imagery" tiles
``.. mf-task-links::``         popular scenarios as link chips
``.. mf-model-hero:: <id>``     chips, hero (image, cost, facts, uses, actions), specs
``.. mf-scenario-cards:: <id>`` cards for the scenarios of one model
``.. mf-scenario:: <id>``       compact hero for one scenario (an option of a model)
``.. mf-cta::``                 "Need a different object?" call to action

Roles
-----
``:mf-icon:`forest```                 decorative monochrome icon
``:mf-chip:`forest|Forest and trees``` white chip, optional icon before ``|``
``:mf-badge:`Default model```          blue chip
``:mf-warn:`On request```              amber chip

Set ``MF_CATALOG_DUMP=1`` to print the generated reStructuredText.
"""

import json
import os
import shutil

from docutils import nodes
from docutils import utils
from docutils.parsers.rst import directives
from docutils.statemachine import StringList
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective

logger = logging.getLogger(__name__)

CATALOG_PATH = os.path.join("_data", "models.json")
IMAGE_DIR = "/_static/models/"

_cache = {}


# ---------------------------------------------------------------- catalog --

def load_catalog(srcdir):
    path = os.path.join(srcdir, CATALOG_PATH)
    mtime = os.path.getmtime(path)
    hit = _cache.get(path)
    if hit and hit[0] == mtime:
        return hit[1]
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    data["_models"] = {m["id"]: m for m in data["models"]}
    data["_scenarios"] = {s["id"]: s for s in data["scenarios"]}
    data["_categories"] = {c["id"]: c for c in data["categories"]}
    _validate(data, srcdir)
    _cache[path] = (mtime, data)
    return data


def _validate(data, srcdir):
    img_root = os.path.join(srcdir, IMAGE_DIR.strip("/"))
    for m in data["models"]:
        if m["category"] not in data["_categories"]:
            logger.warning("models.json: model %s has unknown category %s", m["id"], m["category"])
        if not os.path.exists(os.path.join(img_root, m["image"])):
            logger.warning("models.json: image missing for %s: %s", m["id"], m["image"])
        for sid in m.get("scenarios", []):
            if sid not in data["_scenarios"]:
                logger.warning("models.json: model %s lists unknown scenario %s", m["id"], sid)
    for s in data["scenarios"]:
        if s["model"] not in data["_models"]:
            logger.warning("models.json: scenario %s points to unknown model %s", s["id"], s["model"])


# ------------------------------------------------------------- formatting --

def esc(text):
    """Escape inline markup characters in catalog text."""
    if text is None:
        return ""
    for ch in ("\\", "*", "`", "|"):
        text = text.replace(ch, "\\" + ch)
    return text


def img(name):
    return IMAGE_DIR + name


def base_price(model):
    return (model.get("price") or {}).get("per_km2")


def scenario_price(cat, scenario):
    model = cat["_models"][scenario["model"]]
    base = base_price(model)
    if base is None:
        return None
    return base + (scenario.get("price") or {}).get("option_per_km2", 0)


def example_cost(cat, per_km2, example):
    if per_km2 is None or not example:
        return None
    imagery = cat["imagery_prices"].get(example["imagery"], {})
    data_price = imagery.get(str(example["zoom"]))
    if data_price is None:
        return None
    total = example["area_km2"] * (per_km2 + data_price)
    return "Example: {a} km² on {src} zoom {z} ≈ {t} credits.".format(
        a=example["area_km2"], src=example["imagery"], z=example["zoom"], t=total)


def price_short(model, per_km2):
    if model["availability"] == "custom":
        return "On request"
    if per_km2 is None:
        return (model.get("price") or {}).get("label", "Price shown before you run")
    return "{} cr/km² + imagery".format(per_km2)


def cost_block(cat, model, per_km2, example):
    """-> (main line, note line or None)"""
    price = model.get("price") or {}
    if model["availability"] == "custom":
        return "Priced per project", "Request access and we connect the model to your account."
    if per_km2 is None:
        return price.get("label", "Shown before you run"), price.get("note")
    note = " ".join(x for x in (example_cost(cat, per_km2, example), price.get("note")) if x)
    return "{} credits per km² + imagery".format(per_km2), note or None


def meta_line(model, per_km2, zoom):
    parts = [price_short(model, per_km2)]
    if zoom:
        parts.append("zoom " + zoom)
    return " · ".join(parts)


def chip(icon, text):
    return ":mf-chip:`{}|{}`".format(icon or "", esc(text))


# ------------------------------------------------------------- rst writer --

class Rst:
    """Tiny helper that keeps indentation of generated reStructuredText."""

    def __init__(self):
        self.lines = []
        self.level = 0

    def add(self, text=""):
        pad = "   " * self.level
        for line in (text.split("\n") if text else [""]):
            self.lines.append(pad + line if line else "")

    def blank(self):
        self.lines.append("")

    def open(self, head):
        self.add(head)
        self.blank()
        self.level += 1

    def close(self):
        self.level -= 1
        self.blank()

    def para(self, text, cls=None):
        if cls:
            self.add(".. rst-class:: " + cls)
            self.blank()
        self.add(text)
        self.blank()

    def bullets(self, items, cls=None):
        if cls:
            self.add(".. rst-class:: " + cls)
            self.blank()
        for item in items:
            self.add("* " + item)
        self.blank()


class CatalogDirective(SphinxDirective):
    has_content = False
    optional_arguments = 1
    final_argument_whitespace = False
    wrapper_class = "mf-block"

    @property
    def catalog(self):
        self.env.note_dependency(os.path.join(self.env.srcdir, CATALOG_PATH))
        return load_catalog(self.env.srcdir)

    def build(self, rst):  # pragma: no cover - implemented by subclasses
        raise NotImplementedError

    def run(self):
        rst = Rst()
        self.build(rst)
        if os.environ.get("MF_CATALOG_DUMP"):
            print("\n---- %s (%s)\n%s" % (self.name, self.env.docname, "\n".join(rst.lines)))
        source, line = self.get_source_info()
        content = StringList(rst.lines, items=[(source, line)] * len(rst.lines))
        wrapper = nodes.container(classes=[self.wrapper_class])
        self.set_source_info(wrapper)
        self.state.nested_parse(content, self.content_offset, wrapper)
        return [wrapper]

    def lookup(self, table, key):
        item = self.catalog[table].get(key)
        if item is None:
            raise self.error("unknown id %r in models.json (%s)" % (key, table))
        return item

    # shared pieces ------------------------------------------------------

    def card(self, rst, title, image, alt, link, link_type, chips, desc, meta, extra_cls=""):
        rst.add(".. card:: " + esc(title))
        rst.level += 1
        for opt in (
            ":img-top: " + image if image else None,
            ":img-alt: " + alt if alt else None,
            ":link: " + link,
            ":link-type: " + link_type,
            ":link-alt: " + title,
            ":class-card: mf-card " + extra_cls,
            ":class-img-top: mf-card-img",
            ":class-body: mf-card-body",
            ":class-title: mf-card-title",
        ):
            if opt:
                rst.add(opt.rstrip())
        rst.blank()
        rst.para(" ".join(chips), "mf-card-chips")
        rst.para(esc(desc), "mf-card-desc")
        rst.para(":mf-icon:`credits` " + esc(meta), "mf-card-meta")
        rst.close()

    def hero(self, rst, *, image, alt, caption, cost, description, output, best_with, uses, tip, actions):
        rst.open(".. container:: mf-hero")

        rst.open(".. container:: mf-hero-media")
        rst.add(".. image:: " + image)
        rst.add("   :alt: " + (alt or ""))
        rst.add("   :class: mf-hero-img")
        rst.blank()
        if caption:
            rst.para(esc(caption), "mf-caption")
        main, note = cost
        rst.open(".. container:: mf-cost")
        rst.para("Cost", "mf-label")
        rst.para(esc(main), "mf-cost-main")
        if note:
            rst.para(esc(note), "mf-cost-note")
        rst.close()
        rst.close()

        rst.open(".. container:: mf-hero-body")
        if description:
            rst.para(esc(description), "mf-lede")
        rst.open(".. container:: mf-facts")
        for label, value in (("What you get", output), ("Works best with", best_with)):
            if value:
                rst.open(".. container:: mf-fact")
                rst.para(label, "mf-label")
                rst.para(esc(value))
                rst.close()
        rst.close()
        if uses:
            rst.para("Usage examples", "mf-label")
            rst.bullets([esc(u) for u in uses], "mf-checklist")
        if tip:
            rst.open(".. container:: mf-tip")
            rst.para("**Tip.** " + esc(tip))
            rst.close()
        if actions:
            rst.bullets(actions, "mf-actions")
        rst.close()

        rst.close()


# ------------------------------------------------------------- directives --

class ModelGallery(CatalogDirective):
    """Cards for all models of one availability group."""

    option_spec = {"availability": directives.unchanged}
    wrapper_class = "mf-gallery"

    def build(self, rst):
        cat = self.catalog
        wanted = [a.strip() for a in self.options.get("availability", "default").split(",")]
        rst.open(".. container:: mf-grid")
        for m in cat["models"]:
            if m["availability"] not in wanted:
                continue
            category = cat["_categories"][m["category"]]
            chips = [chip(m.get("icon") or category.get("icon"), category["label"])]
            if m["availability"] == "custom":
                chips.append(":mf-warn:`On request`")
            elif m["availability"] == "no-ai":
                chips.append(":mf-badge:`No AI model`")
            self.card(
                rst,
                title=m["name"],
                image=img(m["image"]),
                alt=m.get("image_alt"),
                link="/" + m["doc"],
                link_type="doc",
                chips=chips,
                desc=m["summary"],
                meta=meta_line(m, base_price(m), m.get("zoom")),
            )
        rst.close()


class WorkflowGallery(CatalogDirective):
    """Tiles for workflows that work with any model (own imagery, search)."""

    wrapper_class = "mf-gallery"

    def build(self, rst):
        rst.open(".. container:: mf-grid")
        for w in self.catalog["workflows"]:
            rst.add(".. card:: " + esc(w["title"]))
            rst.level += 1
            for opt in (":link: /" + w["doc"], ":link-type: doc", ":link-alt: " + w["title"],
                        ":class-card: mf-card mf-card-tile mf-tile-" + w["tile"],
                        ":class-body: mf-card-body", ":class-title: mf-card-title"):
                rst.add(opt)
            rst.blank()
            rst.para(":mf-chip:`uav|Any model`", "mf-card-chips")
            rst.para(esc(w["summary"]), "mf-card-desc")
            rst.para(":mf-icon:`credits` " + esc(w["meta"]), "mf-card-meta")
            rst.close()
        rst.close()


class TaskLinks(CatalogDirective):
    """Popular scenarios as a row of link chips."""

    wrapper_class = "mf-tasks-block"

    def build(self, rst):
        cat = self.catalog
        items = []
        for s in cat["scenarios"]:
            if not s.get("popular"):
                continue
            model = cat["_models"][s["model"]]
            if s.get("option"):
                items.append(":ref:`{} <scenario-{}>`".format(esc(s["title"]), s["id"]))
            else:
                items.append(":doc:`{} </{}>`".format(esc(s["title"]), model["doc"]))
        rst.bullets(items, "mf-tasks")


class ModelHero(CatalogDirective):
    required_arguments = 1
    optional_arguments = 0
    wrapper_class = "mf-model"

    def actions(self, m):
        links = self.catalog["links"]
        if m["availability"] == "custom":
            return [
                "`Request access <{}>`__".format(links["custom_models"]),
                ":doc:`How custom models work </userguides/custom_pipelines>`",
            ]
        return [
            "`Run in Mapflow Web <{}>`__".format(links["web_app"]),
            ":doc:`Use in QGIS </api/qgis_mapflow>`",
            ":doc:`Pricing </userguides/prices>`",
        ]

    def build(self, rst):
        cat = self.catalog
        m = self.lookup("_models", self.arguments[0])
        category = cat["_categories"][m["category"]]

        chips = [chip(m.get("icon") or category.get("icon"), category["label"])]
        chips.append({
            "default": ":mf-badge:`Default model`",
            "custom": ":mf-warn:`On request`",
            "no-ai": ":mf-badge:`No AI model`",
        }[m["availability"]])
        rst.para(" ".join(chips), "mf-chips")

        price = m.get("price") or {}
        self.hero(
            rst,
            image=img(m["image"]),
            alt=m.get("image_alt"),
            caption=m.get("caption"),
            cost=cost_block(cat, m, base_price(m), price.get("example")),
            description=m.get("description"),
            output=m.get("output"),
            best_with=m.get("best_with"),
            uses=m.get("uses"),
            tip=m.get("tip"),
            actions=self.actions(m),
        )

        specs = m.get("specs") or {}
        if specs:
            rst.add(".. rst-class:: mf-specs")
            rst.blank()
            for key, label in cat["labels"].items():
                if specs.get(key):
                    rst.add(":{}: {}".format(label, esc(specs[key])))
            rst.blank()


class ScenarioCards(CatalogDirective):
    required_arguments = 1
    optional_arguments = 0
    wrapper_class = "mf-gallery"

    def build(self, rst):
        cat = self.catalog
        m = self.lookup("_models", self.arguments[0])
        rst.open(".. container:: mf-grid")
        for sid in m.get("scenarios", []):
            s = cat["_scenarios"][sid]
            if s.get("option"):
                chips = [":mf-badge:`+ {}`".format(esc(s["option"]))]
                link, link_type = "scenario-" + s["id"], "ref"
                image, alt = img(s["image"]), s.get("image_alt")
            else:
                chips = [chip(m.get("icon"), "Default run")]
                link, link_type = "/" + m["doc"], "doc"
                image, alt = img(m["image"]), m.get("image_alt")
            self.card(
                rst,
                title=s["title"],
                image=image,
                alt=alt,
                link=link,
                link_type=link_type,
                chips=chips,
                desc=s["summary"],
                meta=meta_line(m, scenario_price(cat, s), s.get("zoom") or m.get("zoom")),
            )
        rst.close()


class Scenario(CatalogDirective):
    required_arguments = 1
    optional_arguments = 0
    wrapper_class = "mf-scenario"

    def build(self, rst):
        cat = self.catalog
        s = self.lookup("_scenarios", self.arguments[0])
        m = cat["_models"][s["model"]]
        rst.para(" ".join([chip(m.get("icon"), m["name"]),
                           ":mf-badge:`+ {}`".format(esc(s["option"]))]), "mf-chips")
        per_km2 = scenario_price(cat, s)
        self.hero(
            rst,
            image=img(s["image"]),
            alt=s.get("image_alt"),
            caption=None,
            cost=cost_block(cat, m, per_km2, (s.get("price") or {}).get("example")),
            description=s.get("description"),
            output=s.get("output"),
            best_with=s.get("best_with"),
            uses=s.get("uses"),
            tip=s.get("tip"),
            actions=None,
        )


class CallToAction(CatalogDirective):
    wrapper_class = "mf-cta"

    def build(self, rst):
        links = self.catalog["links"]
        rst.para("Need a different object?", "mf-cta-title")
        rst.para("We train custom models on your imagery and classes, "
                 "and connect them to your Mapflow account.")
        rst.bullets([
            "`Request a custom model <{}>`__".format(links["custom_models"]),
            "`Model catalog and deployment options <{}>`__".format(links["website_models"]),
            ":doc:`All AI-mapping models </userguides/pipelines>`",
        ], "mf-actions")


# ------------------------------------------------------ gallery headings --

class mf_heading(nodes.rubric):
    """A real <h2> that is not a section, so it stays out of the sidebar TOC."""


def visit_mf_heading_html(self, node):
    self.body.append(self.starttag(node, "h2", "", CLASS="mf-heading"))


def depart_mf_heading_html(self, node):
    self.body.append("</h2>\n")


def visit_mf_heading_other(self, node):
    self.visit_rubric(node)


def depart_mf_heading_other(self, node):
    self.depart_rubric(node)


class Heading(SphinxDirective):
    """``.. mf-heading:: Default models`` with an optional ``:name:`` anchor.

    Gallery pages group cards under headings. Section titles would each become
    an entry in the RTD sidebar next to the child pages; this keeps the h2 for
    screen readers and in-page anchors without touching the navigation.
    """

    required_arguments = 1
    final_argument_whitespace = True
    has_content = False
    option_spec = {"name": directives.unchanged}

    def run(self):
        text = self.arguments[0]
        textnodes, messages = self.state.inline_text(text, self.lineno)
        node = mf_heading(text, "", *textnodes)
        self.set_source_info(node)
        anchor = self.options.get("name") or nodes.make_id(text)
        node["ids"].append(anchor)
        return [node] + messages


# ------------------------------------------------------------------ roles --

def _icon_node(name):
    return nodes.inline("", "", classes=["mf-ico", "mf-ico-" + name])


def icon_role(name, rawtext, text, lineno, inliner, options=None, content=None):
    return [_icon_node(utils.unescape(text).strip())], []


def _chip_role(kind):
    def role(name, rawtext, text, lineno, inliner, options=None, content=None):
        icon, _, label = utils.unescape(text).rpartition("|")
        node = nodes.inline(rawtext, "", classes=["mf-chip", "mf-chip-" + kind])
        if icon.strip():
            node += _icon_node(icon.strip())
        node += nodes.Text(label)
        return [node], []
    return role


# ------------------------------------------------------------- publishing --

def copy_catalog(app, exception):
    """Publish the catalog next to the HTML so other projects can fetch it."""
    if exception or app.builder.format != "html":
        return
    src = os.path.join(app.srcdir, CATALOG_PATH)
    shutil.copyfile(src, os.path.join(app.outdir, "models.json"))


def setup(app):
    app.add_directive("mf-model-gallery", ModelGallery)
    app.add_directive("mf-workflow-gallery", WorkflowGallery)
    app.add_directive("mf-task-links", TaskLinks)
    app.add_directive("mf-model-hero", ModelHero)
    app.add_directive("mf-scenario-cards", ScenarioCards)
    app.add_directive("mf-scenario", Scenario)
    app.add_directive("mf-cta", CallToAction)
    app.add_directive("mf-heading", Heading)
    other = (visit_mf_heading_other, depart_mf_heading_other)
    app.add_node(mf_heading, html=(visit_mf_heading_html, depart_mf_heading_html),
                 latex=other, text=other, man=other, texinfo=other)
    app.add_role("mf-icon", icon_role)
    app.add_role("mf-chip", _chip_role("plain"))
    app.add_role("mf-badge", _chip_role("info"))
    app.add_role("mf-warn", _chip_role("warn"))
    app.connect("build-finished", copy_catalog)
    return {"version": "0.1", "parallel_read_safe": True, "parallel_write_safe": True}
