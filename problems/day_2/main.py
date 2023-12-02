import os
import sys
import time
import colorama
from pathlib import Path
import json
from math import prod
from collections import defaultdict

# fmt: off
sys.path.append(str(Path(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))).parent / 'utils/'))
from utils import time_function, average_time_function
# fmt: on


@average_time_function
def get_constraint(rounds):
    constraint = defaultdict(int)
    for round in rounds:
        for color, value in round.items():
            constraint[color] = max(constraint[color], int(value))
    return dict(constraint)


@time_function
def solve_2(input_data):
    return sum(prod(get_constraint(value).values()) for value in input_data.values())


@average_time_function
def can_be_solved(rounds, constraint):
    return all(int(value) <= constraint[color] for round in rounds for color, value in round.items())


@time_function
def solve(input_data, constraint):
    return sum(int(key) for key, value in input_data.items() if can_be_solved(value, constraint))


@time_function
def parse_input_lines(lines):
    games = {}
    for line in lines:
        game_name, rounds_data = line.strip().split(": ")
        rounds = [round_data.split(", ")
                  for round_data in rounds_data.split("; ")]

        rounds_result = []
        for round_items in rounds:
            round_dict = {item.split(" ")[1]: item.split(" ")[
                0] for item in round_items}
            rounds_result.append(round_dict)

        games[game_name.split("Game ")[-1]] = rounds_result

    return games


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        input_data = parse_input_lines([x.strip() for x in file.readlines()])

    constraints = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 1 is:",
        f"{colorama.Fore.GREEN}{solve(input_data, constraints)}{colorama.Style.RESET_ALL} ===")

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 2 is:",
        f"{colorama.Fore.GREEN}{solve_2(input_data)}{colorama.Style.RESET_ALL} ===")
