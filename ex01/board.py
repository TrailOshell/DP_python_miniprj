#!/usr/bin/python3

import time
import color
import animation

def check_board(board):
    if 'K' not in board:
        animation.typing(f"ERROR: 'K' not in board", clr=color.fg.yellow)
        return 0, 0, False
    elif board.count('K') > 1:
        animation.typing(f"ERROR: multiple 'K' found", clr=color.fg.yellow)
        return 0, 0, False
    
    w, h = 0, 0
    w_max, h_max = 0, 0
    for c in board:
        if c == '\n': break
        w_max += 1
    for c in board:
        if c == '\n':
            if w != w_max:
                animation.typing(f"ERROR: uneven board size (last width = {w}, max width = {w_max})", clr=color.fg.yellow)
                return 0, 0, False
            h += 1; w = 0
        else: w += 1
    h += 1; h_max = h
    return w_max, h_max, True

def create_grid(board, dat):
    w_max, h_max = dat.w_max, dat.h_max
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

def print_grid(dat):
    arr, w_max, h_max = dat.arr, dat.w_max, dat.h_max
    step = 0
    y = 0
    while y < h_max:
        x = 0
        while x < w_max:
            c = arr[y][x]
            print(color_char(c, near_check(dat, x, y)), end='')
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

def print_board(dat):
    arr, w_max, h_max = dat.arr, dat.w_max, dat.h_max
    
    step = 0
    y = 0
    while y < h_max:
        x = 0
        while x < w_max:
            c = arr[y][x]
            print(color_char(c, near_check(dat, x, y)), end='')
            x += 1
        print(f" {h_max - step}\n", end='')
        time.sleep(10000/1000000)
        y += 1
        step += 1
    step = 0
    for c in arr[0]:
        print(f"{chr(ord('A') + step)}", end='')
        step += 1
        if step == 26: step = 0
    print('\n', end='')

def near_check(dat, cx, cy):
    arr, w_max, h_max = dat.arr, dat.w_max, dat.h_max
    if arr[cy][cx] in {'P'}:
        if (arr[cy - (cy != 0)][cx - (cx != 0)] == 'K' or
            arr[cy - (cy != 0)][cx + (cx < w_max)] == 'K'):
            return True

    if arr[cy][cx] not in {'R', 'B', 'Q'}: return False
    target = {'K', '-'}
    if arr[cy][cx] in {'R', 'Q'}:
        for dx, dy in [(-1, 0), (1, 0)]:
            x, y = cx + dx, cy + dy
            if not (0 <= x < w_max and 0 <= y < h_max): continue
            if arr[y][x] in target: return True
    target = {'K', '|'}
    if arr[cy][cx] in {'R', 'Q'}:
        for dx, dy in [(0, -1), (0, 1)]:
            x, y = cx + dx, cy + dy
            if not (0 <= x < w_max and 0 <= y < h_max): continue
            if arr[y][x] in target: return True
    target = {'K', '\\'}
    if arr[cy][cx] in {'B', 'Q'}:
        for dx, dy in [(-1, -1), (1, 1)]:
            x, y = cx + dx, cy + dy
            if not (0 <= x < w_max and 0 <= y < h_max): continue
            if arr[y][x] in target: return True
    target = {'K', '/'}
    if arr[cy][cx] in {'B', 'Q'}:
        for dx, dy in [(1, -1), (-1, 1)]:
            x, y = cx + dx, cy + dy
            if not (0 <= x < w_max and 0 <= y < h_max): continue
            if arr[y][x] in target: return True
    return False

def color_char(char, check):
    color_c = color.style.reset
    if char in {'-', '|', '\\', '/'} or check == True:
        if char in {'P', 'R', 'B', 'Q'}: color_c = f"{color.fg.yellow}{color.bg.orange}"
        else: color_c = color.fg.yellow
    elif char == 'K': color_c = f"{color.fg.black}{color.bg.lightgrey}"
    elif char == 'P': color_c = f"{color.fg.cyan}"
    elif char == 'R': color_c = f"{color.fg.cyan}"
    elif char == 'B': color_c = f"{color.fg.cyan}"
    elif char == 'Q': color_c = f"{color.fg.cyan}"

    output = f"{color_c}{char}{color.style.reset}"
    return output

def draw_line(dat, cx, cy):
    arr, k = dat.arr, dat.k
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