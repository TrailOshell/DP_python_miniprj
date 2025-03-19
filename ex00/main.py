#!/usr/bin/python3

from checkmate import checkmate

def main():
    print("A board")
    board = """\
R...
.K.Q
....
....\
"""
    checkmate(board)

    print()
    print("4x6 board")
    board = """\
R.....
.K...Q
......
......\
"""
    checkmate(board)

    print()
    print("Uneven board")
    board = """\
 R...
.K.Q
....
....\
"""
    checkmate(board)

    print()
    print("Failed check")
    board = """\
....
.K..
....
..P.\
"""
    checkmate(board)

    print()
    print("Pattern out of bound")
    board = """\
....
.K..
....
...P\
"""
    checkmate(board)

if __name__ == "__main__":
    main()
