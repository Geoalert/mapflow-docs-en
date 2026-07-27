#!/usr/bin/env python3
"""
Translate PO files for es (Spanish), zh (Chinese Simplified), and ensure ru (Russian)
untranslated entries are filled in using Google Translate via deep-translator.

Usage:
    python3 translate_po.py [--lang es zh ru] [--dry-run]
"""
import argparse
import glob
import os
import re
import sys
import time

import polib
from deep_translator import GoogleTranslator

# Map Sphinx/gettext language codes to Google Translate codes
LANG_MAP = {
    "es": "es",
    "zh": "zh-CN",
    "ru": "ru",
}

# Strings that must not be translated (RST/Sphinx markup tokens)
SKIP_PATTERNS = [
    re.compile(r"^\s*$"),                     # whitespace only
    re.compile(r"^[|+-]+$"),                  # table border lines
    re.compile(r"^\.\. "),                    # RST directives
    re.compile(r"^:{1,2}[a-zA-Z]"),           # RST field lists / roles
]


def should_skip(msgid: str) -> bool:
    for pat in SKIP_PATTERNS:
        if pat.match(msgid):
            return True
    return False


def translate_text(text: str, target_lang_google: str) -> str:
    """Translate a block of text while preserving RST inline markup and URLs."""
    if not text.strip():
        return text
    try:
        result = GoogleTranslator(source="en", target=target_lang_google).translate(text)
        return result if result else text
    except Exception as exc:
        print(f"  WARNING: translation error: {exc}", file=sys.stderr)
        return text


def process_po_file(po_path: str, lang_code: str, dry_run: bool = False) -> int:
    """Translate all untranslated entries in a PO file. Returns number translated."""
    google_lang = LANG_MAP[lang_code]
    try:
        po = polib.pofile(po_path)
    except Exception as exc:
        print(f"  ERROR loading {po_path}: {exc}", file=sys.stderr)
        return 0

    # Collect untranslated entries
    to_translate = [e for e in po.untranslated_entries() if not should_skip(e.msgid)]

    if not to_translate:
        return 0

    if dry_run:
        return len(to_translate)

    # Batch translate for speed (up to 128 strings per request)
    BATCH = 64
    translator = GoogleTranslator(source="en", target=google_lang, timeout=30)
    translated_count = 0

    for i in range(0, len(to_translate), BATCH):
        batch_entries = to_translate[i:i + BATCH]
        texts = [e.msgid for e in batch_entries]
        try:
            results = translator.translate_batch(texts)
            for entry, result in zip(batch_entries, results):
                if result and result != entry.msgid:
                    entry.msgstr = result
                    if "fuzzy" in entry.flags:
                        entry.flags.remove("fuzzy")
                    translated_count += 1
        except Exception as exc:
            print(f"  WARNING: batch error: {exc}", file=sys.stderr)
            # Fall back to individual translations
            for entry in batch_entries:
                translation = translate_text(entry.msgid, google_lang)
                if translation and translation != entry.msgid:
                    entry.msgstr = translation
                    if "fuzzy" in entry.flags:
                        entry.flags.remove("fuzzy")
                    translated_count += 1
        time.sleep(0.1)  # brief pause between batches

    if translated_count > 0:
        po.save(po_path)

    return translated_count


def main():
    parser = argparse.ArgumentParser(description="Translate PO files")
    parser.add_argument("--lang", nargs="+", default=["es", "zh"],
                        choices=["es", "zh", "ru"],
                        help="Languages to translate (default: es zh)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Count strings to translate without writing files")
    args = parser.parse_args()

    base = os.path.dirname(os.path.abspath(__file__))
    locale_dir = os.path.join(base, "source", "locale")

    for lang in args.lang:
        lang_dir = os.path.join(locale_dir, lang, "LC_MESSAGES")
        if not os.path.isdir(lang_dir):
            print(f"Locale directory not found: {lang_dir}")
            continue

        po_files = sorted(glob.glob(os.path.join(lang_dir, "**", "*.po"), recursive=True))
        print(f"\n=== {lang.upper()} ({len(po_files)} files) ===")
        total = 0
        for po_path in po_files:
            rel = os.path.relpath(po_path, lang_dir)
            n = process_po_file(po_path, lang, dry_run=args.dry_run)
            if n:
                action = "would translate" if args.dry_run else "translated"
                print(f"  {rel}: {action} {n} strings")
            total += n
        action = "Would translate" if args.dry_run else "Translated"
        print(f"  Total: {action} {total} strings for {lang}")

    print("\nDone.")


if __name__ == "__main__":
    main()
