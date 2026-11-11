#!/usr/bin/env python3
"""make.fun news-summary-01 entry: write the bundled summary to /output/entry.txt.

Python 3.13, standard library only. No network. Deterministic: the bundled
summary.txt is copied byte-for-byte, so every run writes identical bytes.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "summary.txt")
DST = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
