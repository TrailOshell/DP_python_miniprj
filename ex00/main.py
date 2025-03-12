#!/usr/bin/python3

# If someone want to play a strict guy. Here's the "Write a function" without an "s"
def checkmate(board):
# try:
    if 'K' not in board:
        return print("ERROR: 'K' not in board")
    elif board.count('K') > 1:
        return print("ERROR: multiple 'K' found")

    w, h = 0, 0
    w_max, h_max = 0, 0
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
                k = [w, h]
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
    
    l_max, r_max = k[0], w_max - (k[0] + 1)
    u_max, d_max = k[1], h_max - (k[1] + 1)
    print(f"King position: {k[0]} {k[1]}")
    print(f"max steps:\tl {l_max} r {r_max} u {u_max} d {d_max}")

    if d_max >= 1 and (
        arr[k[0] - (l_max >= 1)][k[1] + 1] == 'P' or
        arr[k[0] + (r_max >= 1)][k[1] + 1] == 'P'
    ):
        print("A pawn is checking the king")
        checkmate = 1
    
    l, r, u, d = k[0], k[0], k[1], k[1]

    step = 1
    while step <= l_max or step <= r_max or step <= u_max or step <= d_max:
        if step <= l_max: l -= 1
        if step <= r_max: r += 1
        if step <= u_max: u -= 1
        if step <= d_max: d += 1
        print(f"step {step}:\t\tl {l} r {r} u {u} d {d}")
        if arr[l][k[1]] == 'R' or arr[l][k[1]] == 'Q': checkmate = 1
        elif arr[l][k[1]] != '.': l_max = step
        if arr[r][k[1]] == 'R' or arr[r][k[1]] == 'Q': checkmate = 1
        elif arr[r][k[1]] != '.': r_max = step
        if arr[k[0]][u] == 'R' or arr[k[0]][u] == 'Q': checkmate = 1
        elif arr[k[0]][u] != '.': u_max = step
        if arr[k[0]][d] == 'R' or arr[k[0]][d] == 'Q': checkmate = 1
        elif arr[k[0]][d] != '.': d_max = step
        if arr[l][u] == 'B' or arr[l][u] == 'Q': checkmate = 1
        elif arr[l][u] != '.': l_max, u_max = step, step
        if arr[r][u] == 'B' or arr[r][u] == 'Q': checkmate = 1                       
        elif arr[r][u] != '.': r_max, u_max = step, step
        if arr[l][d] == 'B' or arr[l][d] == 'Q': checkmate = 1                       
        elif arr[l][d] != '.': l_max, d_max = step, step
        if arr[r][d] == 'B' or arr[r][d] == 'Q': checkmate = 1
        elif arr[r][d] != '.': r_max, d_max = step, step
        step += 1

    if checkmate == 1:
        return print("Success")
    elif checkmate == 0:
        return print("Fail")
# except:
    return print("Error")

def main():
    board = """\
R...
.K.R
....
....\
"""
    checkmate(board)

if __name__ == "__main__":
    main()