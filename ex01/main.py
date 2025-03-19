#!/usr/bin/python3

import sys
import color
import animation
from checkmate import checkmate

def main():
    for fpath in sys.argv[1:]:
        file = open(fpath, "r")
        animation.typing(f"reading file: ", clr=color.fg.pink, end="")
        animation.typing(f"{fpath}", end="\n")
        checkmate(file.read())

if __name__ == "__main__":
    main()
