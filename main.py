#!/usr/bin/env python3
"""make.fun news-summary-01 entry: write the bundled summary to /output/entry.txt.

Python 3.13, standard library only. No network. Deterministic: the bundled
summary.txt is copied byte-for-byte, so every run writes identical bytes.
Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output.
The summary is a revised 11 November 2026 world-news brief (1,989 chars),
rebuilt and fact-checked in this session from same-day reporting.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "summary.txt")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.txt")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
