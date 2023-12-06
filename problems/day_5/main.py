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


def get_mapping_for_number(num, values):
    for o, d in values:
        if num in range(o[0], o[1]):
            return num + d[0] - o[0]
    return num


@time_function
def solve_1(seeds, blocks):
    answers = []
    for seed in seeds:
        curr = seed
        for block in blocks:
            curr = get_mapping_for_number(curr, block)
        answers.append(curr)

    return min(answers)


@time_function
def solve_2(seeds, blocks):
    seeds = [(seeds[i], seeds[i]+seeds[i+1])
             for i in range(0, len(seeds), 2)]

    answers = []
    curr_seed_ranges = seeds
    for block in blocks:
        block_ranges = []
        while len(curr_seed_ranges) > 0:
            c = curr_seed_ranges.pop(0)
            curr_ranges_ans = []
            curr_ranges_added = []
            for o, d in block:
                offset = d[0] - o[0]
                if c[0] < o[0]: # c starts before origin starts
                    if c[1] > o[0]: # c ends after origin starts
                        if c[1] < o[1]: # c ends before origin ends
                            curr_ranges_ans.append((o[0]+offset, c[1]+offset)) # Takes up part of range
                            curr_ranges_added.append((o[0], c[1]))
                        else:
                            curr_ranges_ans.append((o[0]+offset, o[1]+offset))
                            curr_ranges_added.append((o[0], o[1]))
                else: # c starts after origin starts
                    if o[1] > c[0]: # origin ends after c starts
                        if c[1] < o[1]: # c ends before origin ends
                            curr_ranges_ans.append((c[0]+offset, c[1]+offset)) # Takes up whole range
                            curr_ranges_added.append((c[0], c[1]))
                        else: # c ends after origin ends
                            curr_ranges_ans.append((c[0]+offset, o[1]+offset)) # Takes up part of range
                            curr_ranges_added.append((c[0], o[1]))

            curr_ranges_added = sorted(curr_ranges_added, key=lambda x: x[0])

            if len(curr_ranges_ans) == 0:
                curr_ranges_ans.append((c[0], c[1]))
            else:
                if curr_ranges_added[0][0] > c[0]: # We need to add a range before the first range
                    curr_ranges_ans.insert(0, (c[0], curr_ranges_added[0][0]))
                if curr_ranges_added[-1][1] < c[1]: # We need to add a range after the last range
                    curr_ranges_ans.append((curr_ranges_added[-1][1], c[1]))
                for i in range(len(curr_ranges_added)-1):
                    if curr_ranges_added[i][1] != curr_ranges_added[i+1][0]: # We need to add a range between two ranges
                        curr_ranges_ans.insert(i+1, (curr_ranges_added[i][1], curr_ranges_added[i+1][0]))

            block_ranges.extend(curr_ranges_ans)
        curr_seed_ranges = block_ranges

    curr_seed_ranges = sorted(curr_seed_ranges, key=lambda x: x[0])
    return min(curr_seed_ranges[0])


@time_function
def parse_input_lines(lines):
    seeds = [int(c) for c in lines[0].split(":")[1].split()]
    lines = [x for x in lines[1:] if x]
    blocks = []
    curr = []
    for line in lines:
        if line and line[0].isdigit():
            curr.append([int(x) for x in line.split()])
        elif curr:
            blocks.append(curr)
            curr = []
    blocks.append(curr)

    map_of_blocks = []
    for block in blocks:
        block_ranges = []
        for v in block:
            o = (v[1], v[1]+v[2])
            d = (v[0], v[0]+v[2])
            block_ranges.append((o, d))
        map_of_blocks.append(block_ranges)

    return seeds, map_of_blocks


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        seeds, blocks = parse_input_lines([x.strip() for x in file.readlines()])

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 1 is:",
        f"{colorama.Fore.GREEN}{solve_1(seeds, blocks)}{colorama.Style.RESET_ALL} ===")

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 2 is:",
        f"{colorama.Fore.GREEN}{solve_2(seeds, blocks)}{colorama.Style.RESET_ALL} ===")
