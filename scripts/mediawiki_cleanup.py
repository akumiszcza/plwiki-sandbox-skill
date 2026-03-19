#!/usr/bin/env python3
"""Lightweight MediaWiki draft helper.

Current scope:
- remove clearly enwiki-only metadata templates
- strip enwiki categories
- leave the rest unchanged

This script is intentionally conservative. Extend only with transformations that are
well-tested and easy to review.
"""

from __future__ import annotations
import re
import sys
from pathlib import Path

REMOVE_PATTERNS = [
    re.compile(r'^\{\{Short description\|.*?\}\}\n?', re.MULTILINE),
    re.compile(r'^\{\{Use mdy dates\|.*?\}\}\n?', re.MULTILINE),
    re.compile(r'^\[\[Category:.*?\]\]\n?', re.MULTILINE),
]


def transform(text: str) -> str:
    out = text
    for pattern in REMOVE_PATTERNS:
        out = pattern.sub('', out)
    return out.rstrip() + '\n'


def main() -> int:
    if len(sys.argv) != 3:
        print('usage: mediawiki_cleanup.py <input> <output>', file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])
    text = src.read_text(encoding='utf-8')
    dst.write_text(transform(text), encoding='utf-8')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
