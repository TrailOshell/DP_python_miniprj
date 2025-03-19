#!/usr/bin/python3

import color
import animation
from board import check_board, create_grid, print_grid, print_board, draw_line

# Finally, bonus mode. Strict guy won't complain about multiple functions right?

class data:
    w = 0
    h = 0
    w_max = 0
    h_max = 0
    k = [0, 0]
    arr = [0]

def step_check(dat):
    arr, w_max, h_max, k = dat.arr, dat.w_max, dat.h_max, dat.k
    checkmate = 0

    l_max, r_max = k[0], w_max - (k[0] + 1)
    u_max, d_max = k[1], h_max - (k[1] + 1)
    print(f"King position: {k[0]} {k[1]}")
    print(f"max steps:\tl {l_max} r {r_max} u {u_max} d {d_max}")

    if (arr[k[1] + (k[1] < h_max)][k[0] - (k[0] != 0)] == 'P' or
        arr[k[1] + (k[1] < h_max)][k[0] + (k[0] < w_max)] == 'P'):
        checkmate = 1; print("A pawn checkmate the king")

    for dx, dy, directions in [(-1, 0, l_max), (1, 0, r_max), (0, -1, u_max), (0, 1, d_max)]:
        x, y = k[0], k[1]
        for _ in range(directions):
            x += dx; y += dy
            if not (0 <= x < w_max and 0 <= y < h_max): break
            if arr[y][x] in {'R', 'Q'}: checkmate = 1; print(f"Straight Check arr[{y}][{x}] = {arr[y][x]}"); draw_line(dat, x, y); break
            elif arr[y][x] != '.': break

    for dx, dy, directions in [(-1, -1, min(l_max, u_max)), (1, -1, min(r_max, u_max)),
                        (-1, 1, min(l_max, d_max)), (1, 1, min(r_max, d_max))]:
        x, y = k[0], k[1]
        for _ in range(directions):
            x += dx; y += dy
            if not (0 <= x < w_max and 0 <= y < h_max): break
            if arr[y][x] in {'B', 'Q'}: checkmate = 1; print(f"Diagonal Check arr[{y}][{x}] = {arr[y][x]}"); draw_line(dat, x, y); break
            elif arr[y][x] != '.': break
    return checkmate

def checkmate(board):
# try:
    dat = data()
    dat.w_max, dat.h_max, result = check_board(board)
    if result == False:
        return

    dat.arr, dat.k = create_grid(board, dat)

    checkmate = step_check(dat)

    delay = 30000
    if checkmate == 1:
        print_board(dat)
        animation.typing(f"Success!!! 🎉", delay, clr=color.fg.green, end="")
    elif checkmate == 0:
        animation.typing(f"Fail... 💀", delay, clr=color.fg.red, end="")
# except:
    #return print(f"{color.fg.yellow}Error{color.style.reset}")