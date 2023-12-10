import os
import sys
import time
import colorama
from pathlib import Path
import math

# fmt: off
sys.path.append(str(Path(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))).parent / 'utils/'))
from utils import time_function, average_time_function
# fmt: on

up = (-1,0)
down = (1,0)
left = (0,-1)
right = (0,1)

# dir (y,x) -> [pipes that can be connected]
conv_table = {
    up: ['|', '7', 'F'], # Top
    down: ['|', 'J', 'L'], # Bottom
    right: ['-', 'J', '7'], # Right
    left: ['-', 'F', 'L'] # Left
}

next_pipe = {'|': [up, down], '-': [left, right], '7': [down, left], 'F': [down, right], 'J': [up, left], 'L': [up, right], '.': []}


def get_connected_pipes(board, start):
    result = []
    result_chars = []
    for y, x in [up, down, left, right]:
        new = (start[0] + y, start[1] + x)
        if not(new[0] < 0 or new[0] >= len(board)) and not(new[1] < 0 or new[1] >= len(board[0])): # Check if in bounds
            allowed = conv_table[(y,x)]
            if board[new[0]][new[1]] in allowed:
                result_chars.append((y,x))
                result.append(new)
    
    if up in result_chars:
        if down in result_chars:
            start_pipe_char = '|'
        elif left in result_chars:
            start_pipe_char = 'J'
        elif right in result_chars:
            start_pipe_char = 'L'
    elif down in result_chars:
        if left in result_chars:
            start_pipe_char = 'F'
        elif right in result_chars:
            start_pipe_char = '7'
    elif left in result_chars:
        if right in result_chars:
            start_pipe_char = '-'

    return result, start_pipe_char


def get_connected_pipe(board, start, prev):
    start_char = board[start[0]][start[1]]
    potential = next_pipe[start_char].copy()
    potential.remove(prev)
    return (start[0] + potential[0][0], start[1] + potential[0][1])


def get_path(board, start):
    (path_start, path_finish), start_pipe_char = get_connected_pipes(input_data, start)
    path = [path_start]
    came_from_direction = (start[0]-path_start[0], start[1]-path_start[1])
    while path[-1] != path_finish:
        path.append(get_connected_pipe(input_data, path[-1], came_from_direction)) 
        came_from_direction = (path[-2][0]-path[-1][0], path[-2][1]-path[-1][1]) # Check second last - last to get direction
    return path, start_pipe_char


@time_function
def solve_1(input_data, start):
    path, _ = get_path(input_data, start)
    result = math.ceil(len(path)/2)
    return result

@time_function
def solve_2(input_data, start):
    path, start_pipe_char = get_path(input_data, start)
    path.append(start)
    input_data[start[0]][start[1]] = start_pipe_char

    tiles_inside = []
    for y in range(len(input_data)):
        is_inside = False
        opened_by = None
        for x in range(len(input_data[0])):
            if ((y,x) not in path):
                if is_inside and (y,x) not in path:
                    tiles_inside.append((y,x))
                continue

            if (input_data[y][x] == '|'):
                is_inside = not is_inside

            elif (input_data[y][x] in ['F', 'L']):
                opened_by = input_data[y][x]

            if (input_data[y][x] == '7'):
                if opened_by != 'F':
                    is_inside = not is_inside
                opened_by = None

            elif (input_data[y][x] == 'J'):
                if opened_by != 'L':
                    is_inside = not is_inside
                opened_by = None

    return len(tiles_inside)


@time_function
def parse_input_lines(lines):
    board = []
    for line in lines:
        board.append([x for x in line])
        for c in line:
            if c == 'S':
                start = (len(board) - 1, line.index(c))
    return board, start


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        input_data, start = parse_input_lines([x.strip() for x in file.readlines()])

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 1 is:",
        f"{colorama.Fore.GREEN}{solve_1(input_data, start)}{colorama.Style.RESET_ALL} ===")

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 2 is:",
        f"{colorama.Fore.GREEN}{solve_2(input_data, start)}{colorama.Style.RESET_ALL} ===")