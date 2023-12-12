import os
import sys
import time
import colorama
from pathlib import Path
from tqdm import tqdm
from functools import lru_cache

# fmt: off
sys.path.append(str(Path(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))).parent / 'utils/'))
from utils import time_function, average_time_function
# fmt: on

@lru_cache(maxsize=None)
def calculate(springs, numbers):
    if springs == '' and numbers==() or numbers == () and '#' not in springs:
        return 1
    if springs == '' and numbers!=() or numbers == () and '#' in springs:
        return 0

    result = 0
    if springs[0] in '.?':
        result += calculate(springs[1:], numbers)

    if springs[0] in '#?':
        if numbers[0] <= len(springs) and '.' not in springs[:numbers[0]]:
            if numbers[0] == len(springs) or springs[numbers[0]] != '#':
                result += calculate(springs[numbers[0]+1:], numbers[1:])

    return result


def solve(input_data, size):
    result = 0
    for line in tqdm(input_data):
        springs, numbers = line.split(' ')[0], line.split(' ')[1].split(',').copy()
        springs = '?'.join([springs]*size)
        numbers = tuple([int(x) for x in numbers]*size)
        result += calculate(springs, numbers)
        
    return result


@time_function
def solve_1(input_data):
    return solve(input_data, 1)

@time_function
def solve_2(input_data):
    return solve(input_data, 5)








@time_function
def parse_input_lines(lines):
    return lines


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        input_data = parse_input_lines([x.strip() for x in file.readlines()])

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 1 is:",
        f"{colorama.Fore.GREEN}{solve_1(input_data)}{colorama.Style.RESET_ALL} ===")

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 2 is:",
        f"{colorama.Fore.GREEN}{solve_2(input_data)}{colorama.Style.RESET_ALL} ===")
