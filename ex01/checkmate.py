#!/usr/bin/python3

from color import colors
from board import check_board, create_grid, print_grid, print_board, draw_line

# Finally, bonus mode. Strict guy won't complain about multiple functions right?
    
def step_check(arr, w_max, h_max, k):
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
            if arr[y][x] in {'R', 'Q'}: checkmate = 1; print(f"Straight Check arr[{y}][{x}] = {arr[y][x]}"); draw_line(arr, k, x, y); break
            elif arr[y][x] != '.': break

    for dx, dy, directions in [(-1, -1, min(l_max, u_max)), (1, -1, min(r_max, u_max)),
                        (-1, 1, min(l_max, d_max)), (1, 1, min(r_max, d_max))]:
        x, y = k[0], k[1]
        for _ in range(directions):
            x += dx; y += dy
            if not (0 <= x < w_max and 0 <= y < h_max): break
            if arr[y][x] in {'B', 'Q'}: checkmate = 1; print(f"Diagonal Check arr[{y}][{x}] = {arr[y][x]}"); draw_line(arr, k, x, y); break
            elif arr[y][x] != '.': break
    return checkmate

def checkmate(board):
# try:
    w_max, h_max, result = check_board(board)
    if result == False:
        return

    arr, k = create_grid(board, w_max, h_max)

    checkmate = step_check(arr, w_max, h_max, k)

    if checkmate == 1:
        print_grid(arr, w_max, h_max)
        return print(colors.fg.green, "Success", colors.reset, sep="")
    elif checkmate == 0:
        return print(colors.fg.red, "Fail", colors.reset, sep="")
# except:
    return print("Error")