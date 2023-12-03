import os
import sys
import time
import colorama
from pathlib import Path
from math import prod

# fmt: off
sys.path.append(str(Path(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))).parent / 'utils/'))
from utils import time_function, average_time_function
# fmt: on


@average_time_function
def get_adjacent_numbers(cords, game_map):
    x, y = cords
    numbers_considered = [[False for char in row] for row in game_map]
    adjacent_numbers = []
    # Check surroundings for numbers
    for i in range(-1, 2):
        for j in range(-1, 2):
            if y+i < 0 or x+j < 0:
                continue

            if game_map[y+i][x+j].isnumeric() and not numbers_considered[y+i][x+j]:
                # Number found, now get adjacent numbers to form full number
                full_number = []
                dixit_x, digit_y = x+j, y+i
                # Check left, from origin outwards, prepend to full_number
                for x_offset in [(0, 0), (-1, 0), [-2, 0]]:
                    if not game_map[digit_y][dixit_x+x_offset[0]].isnumeric():
                        break
                    full_number.insert(
                        0, game_map[digit_y][dixit_x+x_offset[0]])
                    numbers_considered[digit_y][dixit_x +
                                                x_offset[0]] = True
                # Check right, from origin outwards, append to full_number
                for x_offset in [(1, 0), [2, 0]]:
                    if not game_map[digit_y][dixit_x+x_offset[0]].isnumeric():
                        break
                    full_number.append(
                        game_map[digit_y][dixit_x+x_offset[0]])
                    numbers_considered[digit_y][dixit_x +
                                                x_offset[0]] = True
                adjacent_numbers.append(int(''.join(full_number)))
    return adjacent_numbers


@time_function
def solve_1(input_data):
    return sum([int(sum(x[-1])) for x in input_data])


@time_function
def solve_2(input_data):
    return sum([prod(part[2]) for part in input_data if part[1] == '*' and len(part[2]) == 2])


@time_function
def parse_input_lines(lines):
    parts = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if not char.isnumeric() and not char == '.':
                parts.append([(x, y), char, get_adjacent_numbers(
                    cords=(x, y), game_map=lines)])
    return parts


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        input_data = parse_input_lines([x.strip() for x in file.readlines()])

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 1 is:",
        f"{colorama.Fore.GREEN}{solve_1(input_data)}{colorama.Style.RESET_ALL} ===")

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 2 is:",
        f"{colorama.Fore.GREEN}{solve_2(input_data)}{colorama.Style.RESET_ALL} ===")
