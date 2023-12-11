import os
import sys
import time
import colorama
from pathlib import Path
import numpy as np
from tqdm import tqdm

# fmt: off
sys.path.append(str(Path(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))).parent / 'utils/'))
from utils import time_function, average_time_function
# fmt: on


def get_columns_not_containing(input_data, char):
    return [i for i, col in enumerate(input_data) if char not in col]

def calculate_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

@time_function
def solve(input_data, space_size):
    columns_not_containing = get_columns_not_containing(input_data, "#")
    rows_not_containing = get_columns_not_containing(input_data.T, "#")

    print(f"columns_not_containing: {columns_not_containing}")
    print(f"rows_not_containing: {rows_not_containing}")

    pos_not_dot = np.array(np.where(input_data != '.')).T

    all_combinations = {}
    for i in tqdm(range(len(pos_not_dot))):
        for j in range(1, len(pos_not_dot)):
            if i == j:
                continue
            i_cords = list(pos_not_dot[i])
            j_cords = list(pos_not_dot[j])
            if f"{(i_cords, j_cords)}" not in all_combinations and f"{(j_cords, i_cords)}" not in all_combinations:

                ok_range = range(min(i_cords[1], j_cords[1]), max(i_cords[1], j_cords[1]))
                empty_columns_in_between = [r for r in rows_not_containing if r in ok_range]

                ok_range = range(min(i_cords[0], j_cords[0]), max(i_cords[0], j_cords[0]))
                empty_rows_in_between = [c for c in columns_not_containing if c in ok_range]

                all_combinations[f"{(i_cords, j_cords)}"] = calculate_distance(i_cords, j_cords) + (len(empty_columns_in_between)+len(empty_rows_in_between)) * (space_size - 1)

    return sum(all_combinations.values())

@time_function
def solve_1(input_data):
    return solve(input_data, 2)

@time_function
def solve_2(input_data):
    return solve(input_data, 1000000)




@time_function
def parse_input_lines(lines):
    grid = np.empty((len(lines[0]), len(lines)), dtype=str)
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            grid[x][y] = lines[x][y]
    return grid


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        input_data = parse_input_lines([x.strip() for x in file.readlines()])

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 1 is:",
        f"{colorama.Fore.GREEN}{solve_1(input_data)}{colorama.Style.RESET_ALL} ===")

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 2 is:",
        f"{colorama.Fore.GREEN}{solve_2(input_data)}{colorama.Style.RESET_ALL} ===")