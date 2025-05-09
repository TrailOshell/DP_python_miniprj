#!/usr/bin/python3

# If someone want to play a strict guy. Here's the "Write a function" without an "s"
def checkmate(board):
# try:
    if 'K' not in board:
        return print("ERROR: 'K' not in board")
    elif board.count('K') > 1: return print("ERROR: multiple 'K' found")

    w, h = 0, 0
    w_max, h_max = 0, 0
    for c in board:
        if c == '\n': break
        w_max += 1
    for c in board:
        if c == '\n':
            if w != w_max:
                return print(f"ERROR: uneven board size (last width = {w}, max width = {w_max})")
            h += 1; w = 0
        else: w += 1
    h += 1; h_max = h
    if w != h:
        return print(f"ERROR: the board is not square (width = {w}, height = {h})")

    arr = [[0 for i in range(w)] for j in range(h)]
    k = [0, 0]; w, h = 0, 0
    for c in board:
        if c == '\n': h += 1; w = 0
        else:
            if c == 'K': k = [w, h]
            if c in {'K', 'P', 'Q', 'R', 'B'}: arr[h][w] = c
            else: arr[h][w] = '.'
            w += 1

    l_max, r_max = k[0], w_max - (k[0] + 1)
    u_max, d_max = k[1], h_max - (k[1] + 1)

    checkmate = 0
    
    if (arr[k[0] - (l_max >= 1)][k[1] + (d_max >= 1)] == 'P' or
        arr[k[0] + (r_max >= 1)][k[1] + (d_max >= 1)] == 'P'):
        checkmate = 1;

    for dx, dy, directions in [(-1, 0, l_max), (1, 0, r_max), (0, -1, u_max), (0, 1, d_max)]:
        x, y = k[0], k[1]
        for _ in range(directions):
            x += dx; y += dy
            if not (0 <= x < w_max and 0 <= y < h_max): break
            if arr[y][x] in {'R', 'Q'}: checkmate = 1; break
            elif arr[y][x] != '.': break

    for dx, dy, directions in [(-1, -1, min(l_max, u_max)), (1, -1, min(r_max, u_max)),
                        (-1, 1, min(l_max, d_max)), (1, 1, min(r_max, d_max))]:
        x, y = k[0], k[1]
        for _ in range(directions):
            x += dx; y += dy
            if not (0 <= x < w_max and 0 <= y < h_max): break
            if arr[y][x] in {'B', 'Q'}: checkmate = 1; break
            elif arr[y][x] != '.': break
    
    if checkmate == 1: return print("Success")
    elif checkmate == 0: return print("Fail")
# except:
    return print("Error")