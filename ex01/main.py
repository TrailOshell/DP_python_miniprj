# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tsomchan <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/13 11:35:05 by tsomchan          #+#    #+#              #
#    Updated: 2025/03/13 11:35:05 by tsomchan         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/python3

# Finally, bonus mode. Strict guy won't complain about multiple functions right?


class colors:
 
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'
    
    class fg:
            black = '\033[30m'
            red = '\033[31m'
            green = '\033[32m'
            orange = '\033[33m'
            blue = '\033[34m'
            purple = '\033[35m'
            cyan = '\033[36m'
            lightgrey = '\033[37m'
            darkgrey = '\033[90m'
            lightred = '\033[91m'
            lightgreen = '\033[92m'
            yellow = '\033[93m'
            lightblue = '\033[94m'
            pink = '\033[95m'
            lightcyan = '\033[96m'
    
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'
    
def check_board(board):
    if 'K' not in board:
        print("ERROR: 'K' not in board"); return 0, 0, False
    elif board.count('K') > 1:
        print("ERROR: multiple 'K' found"); return 0, 0, False
    
    w, h = 0, 0
    w_max, h_max = 0, 0
    for c in board:
        if c == '\n': break
        w_max += 1
    for c in board:
        if c == '\n':
            if w != w_max:
                print (f"ERROR: uneven board size (last width = {w}, max width = {w_max})")
                return 0, 0, False
            h += 1; w = 0
        else: w += 1
    h += 1; h_max = h
    return w_max, h_max, True

def create_grid(board, w_max, h_max):
    arr = [[0 for i in range(w_max)] for j in range(h_max)]
    k = [0, 0]; w, h = 0, 0
    for c in board:
        if c == '\n': h += 1; w = 0
        else:
            if c == 'K': k = [w, h]
            if c in {'K', 'P', 'Q', 'R', 'B'}: arr[h][w] = c
            else: arr[h][w] = '.'
            w += 1
    return arr, k

def print_grid(arr, w_max, h_max):
    step = 0
    y = 0
    while y < h_max:
        x = 0
        while x < w_max:
            c = arr[y][x]
            print(color_char(c, near_check(arr, x, y, w_max, h_max)), end='')
            x += 1
        print(f" {step}", end='')
        print('\n', end='')
        y += 1
        step += 1
    step = 0
    for c in arr[0]:
        print(f"{step % 10}", end='')
        step += 1
    print('\n', end='')

def print_board(arr, h_max):
    step = 0
    for row in arr:
        for c in row: print(color_char(c, near_check(arr, x, y, w_max, h_max)), end='')
        print(f" {h_max - step}", end='')
        print('\n', end='')
        step += 1
    step = 0
    for c in arr[0]:
        print(f"{chr(ord('a') + step)}", end='')
        step += 1
    print('\n', end='')

def near_check(arr, cx, cy, w_max, h_max):
    if arr[cy][cx] in {'P'}:
        if (arr[cy - (cy != 0)][cx - (cx != 0)] == 'K' or
            arr[cy - (cy != 0)][cx + (cx < w_max)] == 'K'):
            return True

    if arr[cy][cx] not in {'R', 'B', 'Q'}: return False
    target = {'K', '-', '|'}
    if arr[cy][cx] in {'R', 'Q'}:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = cx + dx, cy + dy
            if not (0 <= x < w_max and 0 <= y < h_max): continue
            if arr[y][x] in target: return True
    target = {'K', '\\', '/'}
    if arr[cy][cx] in {'B', 'Q'}:
        for dx, dy in [(-1, -1), (1, -1), (-1, 1), (1, 1)]:
            x, y = cx + dx, cy + dy
            if not (0 <= x < w_max and 0 <= y < h_max): continue
            if arr[y][x] in target: return True
    return False


def color_char(char, check):
    color = colors.reset
    if char in {'-', '|', '\\', '/'} or check == True: color = colors.fg.yellow
    elif char == 'K': color = f"{colors.fg.black}{colors.bg.lightgrey}"
    elif char == 'P': color = f"{colors.fg.cyan}"
    elif char == 'R': color = f"{colors.fg.cyan}"
    elif char == 'B': color = f"{colors.fg.cyan}"
    elif char == 'Q': color = f"{colors.fg.cyan}"

    output = f"{color}{char}{colors.reset}"
    return output

def step_check(arr, w_max, h_max, k):
    checkmate = 0

    l_max, r_max = k[0], w_max - (k[0] + 1)
    u_max, d_max = k[1], h_max - (k[1] + 1)
    print(f"King position: {k[0]} {k[1]}")
    print(f"max steps:\tl {l_max} r {r_max} u {u_max} d {d_max}")

    if (arr[k[1] + (k[1] < h_max)][k[0] - (k[0] != 0)] == 'P' or
        arr[k[1] + (k[1] < h_max)][k[0] + (k[0] < w_max)] == 'P'):
        checkmate = 1; print("A pawn is checking the king")

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

def draw_line(arr, k, cx, cy):
    if cx == k[0]: line = '|'
    elif cy == k[1]: line = '-'
    elif (cx < k[0] and cy < k[1]) or (cx > k[0] and cy > k[1]): line = '\\'
    elif (cx > k[0] and cy < k[1]) or (cx < k[0] and cy > k[1]): line = '/'

    dx, dy = 0, 0
    if cx < k[0]: dx = 1
    elif cx > k[0]: dx = -1
    if cy < k[1]: dy = 1
    elif cy > k[1]: dy = -1

    while cx != k[0] or cy != k[1]:
        cx += dx; cy += dy
        if cx == k[0] and cy == k[1]: break
        arr[cy][cx] = line
    return arr


def checkmate(board):
# try:
    w_max, h_max, result = check_board(board)
    if result == False:
        return

    arr, k = create_grid(board, w_max, h_max)

    # print_grid(arr)
    # print_board(arr, h_max)

    checkmate = step_check(arr, w_max, h_max, k)

    if checkmate == 1: print_grid(arr, w_max, h_max); return print(colors.fg.green, "Success", colors.reset, sep="")
    elif checkmate == 0: return print(colors.fg.red, "Fail", colors.reset, sep="")
# except:
    return print("Error")

def main():
    board = """\
..........R....
...............
...............
...............
...............
..........R....
..P..B.....B...
...............
...............
........KP....Q
.........P.....
...............
.....Q........Q
.....P...P.....
..........Q.QQ.\
"""
    checkmate(board)

if __name__ == "__main__":
    main()