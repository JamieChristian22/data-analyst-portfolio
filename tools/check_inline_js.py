#!/usr/bin/env python3
"""Syntax-check locally embedded JavaScript without executing application code.

Requirements: Python 3.11+ and Node.js on PATH. This validates syntax only,
not browser interactions, data correctness, or accessibility.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess

SCRIPTS = re.compile(r"<script\\b([^>]*)>(.*?)</script\\s*>", re.I | re.S)
JSON_SCRIPT = re.compile(r"""\\btype\\s*=\\s*(['"])application/json\\1""", re.I)
SRC = re.compile(r"\\bsrc\\s*=", re.I)


def check(html_path: Path) -> None:
    if not html_path.is_file():
        raise ValueError(f"Missing HTML demo: {html_path}")
    markup = html_path.read_text(encoding="utf-8")
    scripts = []
    for attrs, source in SCRIPTS.findall(markup):
        if SRC.search(attrs):
            raise ValueError(f"{html_path}: external script is not permitted")
        if JSON_SCRIPT.search(attrs):
            continue
        if source.strip():
            scripts.append(source)
    if not scripts:
        raise ValueError(f"{html_path}: no executable inline JavaScript found")
    for index, source in enumerate(scripts, 1):
        result = subprocess.run(
            ["node", "--check", "-"], input=source, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            check=False, timeout=20,
        )
        if result.returncode:
            raise ValueError(
                f"{html_path}: inline script {index} is invalid:\n{result.stderr}"
            )
    print(f"PASS: {html_path} — {len(scripts)} executable inline script(s) parse")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", nargs="+", type=Path)
    args = parser.parse_args()
    for path in args.html:
        check(path)


if __name__ == "__main__":
    main()
