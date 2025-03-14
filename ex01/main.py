#!/usr/bin/python3

import sys
from checkmate import checkmate
from color import colors

def main():
    for fpath in sys.argv[1:]:
        file = open(fpath, "r")
        print(f"{colors.fg.pink}reading file: {colors.reset}{fpath}")
        checkmate(file.read())

if __name__ == "__main__":
    main()