#!/usr/bin/python3

import sys
from checkmate import checkmate

def main():
    for fpath in sys.argv[1:]:
        file = open(fpath, "r")
        print(f"reading file: {fpath}")
        checkmate(file.read())

if __name__ == "__main__":
    main()