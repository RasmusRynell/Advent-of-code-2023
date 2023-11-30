import sys
import time

from utils import time_function, average_time_function

@time_function
def solve_problem(input_data):
    result = input_text
    return result

@time_function
def parse_input(input_text):
    result = input_text
    return result

if __name__ == '__main__':
    with open('inputs/simple_input.txt', 'r') as file:
        input_text = file.read()
    input_data = parse_input(input_text)
    solution = solve_problem(input_data)
    print(f"=== The solution is: {solution} ===")