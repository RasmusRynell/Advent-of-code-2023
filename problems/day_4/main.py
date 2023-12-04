import os
import sys
import time
import colorama
from pathlib import Path
import json

# fmt: off
sys.path.append(str(Path(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))).parent / 'utils/'))
from utils import time_function, average_time_function
# fmt: on


@time_function
def solve_1(input_data):
    def wins(game):
        result = 0
        for number in game['my']:
            if number in game['correct']:
                result = 1 if not result else result * 2
        return result

    return sum([wins(game) for game in input_data])


@time_function
def solve_2(input_data):
    instances = [1 for _ in input_data]
    for i, game in enumerate(input_data):
        for _ in range(1, instances[i]+1):
            num_of_correct = 0
            for number in game['my']:
                if number in game['correct']:
                    num_of_correct += 1
            for j in range(1, num_of_correct+1):
                instances[i+j] += 1
    return sum(instances)


@time_function
def parse_input_lines(lines):
    games = []
    for line in lines:
        l = line.split(':')[1].split(' | ')
        games.append({
            'correct': [int(x) for x in l[0].split()],
            'my': [int(x) for x in l[1].split()]
        })
    return games


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        input_data = parse_input_lines([x.strip() for x in file.readlines()])

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 1 is:",
        f"{colorama.Fore.GREEN}{solve_1(input_data)}{colorama.Style.RESET_ALL} ===")

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 2 is:",
        f"{colorama.Fore.GREEN}{solve_2(input_data)}{colorama.Style.RESET_ALL} ===")
