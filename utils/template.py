import sys
import time
import colorama

from utils import time_function, average_time_function


@time_function
def solve(input_data):
    result = input_data
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
