#!/usr/bin/python3
"""text file-reading."""


def read_file(filename=""):
    """Print the content."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
