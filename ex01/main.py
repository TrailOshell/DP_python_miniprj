#!/usr/bin/python3

import sys
import color
import animation
from checkmate import checkmate

def main():
    for fpath in sys.argv[1:]:
        file = open(fpath, "r")
        color.change(color.fg.pink)
        animation.typing(f"reading file: ", end="")
        color.change(color.style.reset)
        animation.typing(f"{fpath}")
        checkmate(file.read())

if __name__ == "__main__":
    main()