#!/usr/bin/python3

def check_board(board):
    if 'K' not in board:
        return "ERROR: 'K' not in board"
    w = 0
    h = 0
    w_max = 0
    for c in board:
        w_max += 1
        if c == '\n':
            break
    for c in board:
        if c == '\n':
            h += 1
            if w != w_max:
                return f"ERROR: uneven board size (width {w} and width {w_max})"

        else:
            w += 1
    return board

def main():
    board = """\
    R...
    .K..
    ..P.
    ....\
    """
    print("run")
    print(check_board(board))
    # checkmate(board)

if __name__ == "__main__":
    main()

# try:
#     if __name__ == "__main__":
#         main()

# except:
#     print("ERROR")