import os
import sys
import time
import colorama
from pathlib import Path
import time

# fmt: off
sys.path.append(str(Path(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))).parent / 'utils/'))
from utils import time_function, average_time_function
# fmt: on


def get_new_num(num, values):
    for value in values:
        #print(f"Num: {num}, Values: {value}")
        if value[1] <= num < (value[1] + value[2]):
            #print(f"{value[1]} <= {num} < {value[1] + value[2]} Found {value[0] + num-value[1]}")
            return value[0] + num-value[1]
    #print("Not found", num)
    return num

@time_function
def solve_1(input_data):
    result = 1000000000000
    for seed in input_data['seeds']:
        current = "seed"
        num = seed
        #print("Seed: ", seed)
        for key, value in input_data.items():
            if key == "seeds":
                continue
            if value['from'] == current:
                num = get_new_num(num, value['values'])
                current = value['to']
            #print("Key: ", key, num)
        #print("Last: ", num, "====\n")
        if num < result:
            result = num
    
    return result

@time_function
def solve_2(input_data):
    result = 100000000000000000

    cache = {}

    for i in range(0, len(input_data['seeds']), 2):
        print("Range ", input_data['seeds'][i], input_data['seeds'][i]+input_data['seeds'][i+1])
        for seed in range(input_data['seeds'][i], input_data['seeds'][i]+input_data['seeds'][i+1]):
            if seed in cache:
                break
            current = "seed"
            num = seed
            print("Seed: ", seed)
            largest = 0
            for key, value in input_data.items():
                if key == "seeds":
                    continue
                if value['from'] == current:
                    out_num = get_new_num(num, value['values'])
                    current = value['to']
                #print("Key: ", key, num)
            print("Last: ", out_num)
            cache[seed] = out_num
            if out_num < result:
                result = out_num
            print("result: ", result)
            print("=")
            if seed > largest:
                break
        print("===")

    
    return result






@time_function
def parse_input_lines(lines):
    result = {}

    current_map_name = ""
    for line in lines:
        if not line:
            continue
        if line.startswith("seeds"):
            result['seeds'] = [int(x) for x in line.split(":")[1].split()]
        elif line[0].isdigit():
            result[current_map_name]['values'].append([int(x) for x in line.split()])
        else:
            current_map_name = line.split()[0]
            my_from, _, my_to = current_map_name.split('-')
            result[current_map_name] = {}
            result[current_map_name]['values'] = []
            result[current_map_name]['from'] = my_from
            result[current_map_name]['to'] = my_to
    return result


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        input_data = parse_input_lines([x.strip() for x in file.readlines()])

    # print(
    #     f"=== For \"{sys.argv[1]}\" the solution for part 1 is:",
    #     f"{colorama.Fore.GREEN}{solve_1(input_data)}{colorama.Style.RESET_ALL} ===")

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 2 is:",
        f"{colorama.Fore.GREEN}{solve_2(input_data)}{colorama.Style.RESET_ALL} ===")
