#!/usr/bin/python3

# If someone want to play a strict guy. Here's the "Write a function" without an "s"
def checkmate(board):
    try:
        if 'K' not in board:
            return "ERROR: 'K' not in board"
            # return "ERROR: multiple 'K' found"

        w = 0
        h = 0
        w_max = 0
        h_max = 0
        for c in board:
            if c == '\n':
                break
            w_max += 1
        for c in board:
            if c == '\n':
                h += 1
                if w != w_max:
                    return f"ERROR: uneven board size (last width = {w}, max width = {w_max})"
                w = 0
            else:
                w += 1
        h += 1
        h_max = h

        rows, cols = (h, w)
        arr = [[0 for i in range(cols)] for j in range(rows)]
        k = [0, 0]
        w = 0
        h = 0
        for c in board:
            # print(f"{h} {w} {c}")
            if c == '\n':
                h += 1
                w = 0
            else:
                if c == 'K':
                    k = [h, w]
                if c == 'K' or c == 'P' or c == 'Q' or c == 'R' or c == 'B':
                    arr[h][w] = c
                else:
                    arr[h][w] = '.'
                w += 1

        for row in arr:
            for c in row:
                print(c, end='')
            print('\n', end='')
        # print(f"K pos is {k_pos[0]} {k_pos[1]}")

        checkmate = 0

        
        step = 1
        left_max = k[0]
        right_max = w_max - (k[0] + 1)
        up_max = k[1]
        down_max = h_max - (k[1] + 1)
        print(f"King position: {k[0]} {k[1]}")
        print(f"max steps:\tl {left_max} r {right_max} u {up_max} d {down_max}")

        if arr[k[0] - 1][k[1] + 1] == 'P' or arr[k[0] + 1][k[1] + 1] == 'P':
            print("A pawn is checking the king")
            checkmate = 1
        
        l = k[0]
        r = k[0]
        u = k[1]
        d = k[1]
        while step <= left_max or step <= right_max or step <= up_max or step <= down_max:
            if step <= left_max:
                l -= 1
            if step <= right_max:
                r += 1
            if step <= up_max:
                u -= 1
            if step <= down_max:
                d += 1
            print(f"step {step}:\t\tl {l} r {r} u {u} d {d}")
            if arr[l][k[1]] == 'R' or arr[l][k[1]] == 'Q':
                checkmate = 1
            elif arr[l][k[1]] != '.':
                left_max = step
            if arr[r][k[1]] == 'R' or arr[r][k[1]] == 'Q':
                checkmate = 1
            elif arr[r][k[1]] != '.':
                right_max = step
            if arr[k[0]][u] == 'R' or arr[k[0]][u] == 'Q':
                checkmate = 1
            elif arr[k[0]][u] != '.':
                up_max = step
            if arr[k[0]][d] == 'R' or arr[k[0]][d] == 'Q':
                checkmate = 1
            elif arr[k[0]][d] != '.':
                down_max = step
            if arr[l][u] == 'B' or arr[l][u] == 'Q':
                checkmate = 1
            elif arr[l][u] != '.':
                left_max = step
                up_max = step
            if arr[r][u] == 'B' or arr[r][u] == 'Q':
                checkmate = 1                       
            elif arr[r][u] != '.':
                right_max = step
                up_max = step
            if arr[l][d] == 'B' or arr[l][d] == 'Q':
                checkmate = 1                       
            elif arr[l][d] != '.':
                left_max = step
                down_max = step
            if arr[r][d] == 'B' or arr[r][d] == 'Q':
                checkmate = 1
            elif arr[r][d] != '.':
                right_max = step
                down_max = step
            step += 1

        if checkmate == 1:
            return "Success"
        elif checkmate == 0:
            return "Fail"
    except:
        return "Error"

def main():
    board = """\
R...
.K..
..P.
....\
"""
    print(board)
    print(check_board(board))
    checkmate(board)

if __name__ == "__main__":
    main()

# try:
#     if __name__ == "__main__":
#         main()

# except:
#     print("ERROR")