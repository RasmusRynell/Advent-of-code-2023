from pathlib import Path
import colorama
import time
import sys
import os

# fmt: off
sys.path.append(str(Path(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))).parent / 'utils/'))
from utils import time_function, average_time_function
# fmt: on

conv = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}


@time_function
def solve(input_data):
    result = 0
    for word in input_data:
        digits = []
        for i in range(len(word)):
            if word[i].isdigit():
                digits.append(word[i])
            else:
                for conv_word in conv:
                    if word[i:].startswith(conv_word):
                        digits.append(str(conv[conv_word]))
                        break
        result += int(digits[0] + digits[-1])
    return result


@time_function
def parse_input_lines(lines):
    result = lines
    return result


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        input_data = parse_input_lines(file.read().split())

    print(
        f"=== For \"{sys.argv[1]}\" the solution is:",
        f"{colorama.Fore.GREEN}{solve(input_data)}{colorama.Style.RESET_ALL} ===")
