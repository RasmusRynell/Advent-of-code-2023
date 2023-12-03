import os
import sys
import time
import colorama
from pathlib import Path

# fmt: off
sys.path.append(str(Path(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))).parent / 'utils/'))
from utils import time_function, average_time_function
# fmt: on


@time_function
def solve_1(input_data):
    result = input_data
    return result

@time_function
def solve_2(input_data):
    result = input_data
    return result








@time_function
def parse_input_lines(lines):
    result = lines
    return result


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        input_data = parse_input_lines([x.strip() for x in file.readlines()])

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 1 is:",
        f"{colorama.Fore.GREEN}{solve_1(input_data)}{colorama.Style.RESET_ALL} ===")

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 2 is:",
        f"{colorama.Fore.GREEN}{solve_2(input_data)}{colorama.Style.RESET_ALL} ===")