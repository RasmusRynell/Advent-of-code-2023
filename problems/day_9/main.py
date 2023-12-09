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


# Extrapolate forwards
@time_function
def solve_1(input_data):
    result = 0
    for reading in input_data:
        while any(reading[-1]):
            new_line = []
            for i in range(len(reading[-1])-1):
                new_line.append(reading[-1][i+1] - reading[-1][i])
            reading.append(new_line)

        for idx in range(len(reading)-3, -1, -1):
            reading[idx].append(reading[idx][-1] + reading[idx+1][-1])
        result += reading[0][-1]
    return result


# Extrapolate backwards
@time_function
def solve_2(input_data):
    result = 0

    for reading in input_data:
        while any(reading[-1]):
            new_line = []
            for i in range(len(reading[-1])-1):
                new_line.append(reading[-1][i+1] - reading[-1][i])
            reading.append(new_line)
        for idx in range(len(reading)-3, -1, -1):
            reading[idx].insert(0, reading[idx][0] - reading[idx+1][0])
        result += reading[0][0]

    return result







@time_function
def parse_input_lines(lines):
    result = [[[int(x) for x in l.split()]] for l in lines]
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
