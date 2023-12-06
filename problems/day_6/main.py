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
    times = input_data[0]
    distances = input_data[1]

    results = 1
    for i in range(len(times)):
        win_times = 0
        for j in range(times[i]+1):
            hold_down = j
            speed = j
            time_remaining = times[i]-j
            result = speed * time_remaining
            if result > distances[i]:
                win_times += 1

        if win_times > 0:
            results *= win_times

    return results


@time_function
def solve_2(input_data):
    print(input_data)
    return solve_1(input_data)


@time_function
def parse_input_lines(lines):
    times = [int(''.join([x for x in lines[0].split(':')[1].replace(" ", "")]))]
    distances = [int(''.join([x for x in lines[1].split(':')[1].replace(" ", "")]))]
    return (times, distances)


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        input_data = parse_input_lines([x.strip() for x in file.readlines()])

    # print(
    #     f"=== For \"{sys.argv[1]}\" the solution for part 1 is:",
    #     f"{colorama.Fore.GREEN}{solve_1(input_data)}{colorama.Style.RESET_ALL} ===")

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 2 is:",
        f"{colorama.Fore.GREEN}{solve_2(input_data)}{colorama.Style.RESET_ALL} ===")
