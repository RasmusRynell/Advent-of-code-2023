import os
import sys
import time
import colorama
from pathlib import Path
import functools

# fmt: off
sys.path.append(str(Path(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))).parent / 'utils/'))
from utils import time_function, average_time_function
# fmt: on

char_value_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def compare_hands(hand1_in, hand2_in):
    # If 1 < 2, return -1 # Hand 2 is better
    # If 1 = 2, return 0 # Tie
    # If 1 > 2, return 1 # Hand 1 is better
    
    hand1 = hand1_in[0]
    hand2 = hand2_in[0]

    hand1_count={}
    for c in hand1:
        hand1_count[c]=hand1_count.setdefault(c, 0)+1
    hand2_count={}
    for c in hand2:
        hand2_count[c]=hand2_count.setdefault(c, 0)+1


    hand1_values = sorted(hand1_count.values(), reverse=True)
    hand2_values = sorted(hand2_count.values(), reverse=True)
    
    num_unique_cards_hand1 = hand1_values[0]
    num_unique_cards_hand2 = hand2_values[0]

    second_largest_hand1 = hand1_values[1] if len(hand1_values) > 1 else 0
    second_largest_hand2 = hand2_values[1] if len(hand2_values) > 1 else 0


    if num_unique_cards_hand1 > num_unique_cards_hand2: # hand 1 is better
        return 1
    elif num_unique_cards_hand1 < num_unique_cards_hand2: # hand 2 is better
        return -1


    if second_largest_hand1 > second_largest_hand2: # hand 1 is better
        return 1
    elif second_largest_hand1 < second_largest_hand2: # hand 2 is better
        return -1


    for card in zip(hand1, hand2):
        if card[0] == card[1]:
            continue
        if char_value_order.index(card[0]) < char_value_order.index(card[1]): # Hand 1 better
            return 1
        return -1


@time_function
def solve_1(input_data):
    key_func = functools.cmp_to_key(compare_hands)
    result = sorted(input_data, key=key_func)

    res = 0
    for i in range(len(result)):
        res += (i+1)*int(result[i][1])

    return res

@time_function
def solve_2(input_data):
    return input_data








@time_function
def parse_input_lines(lines):
    result = []
    for line in lines:
        result.append(line.split(' '))
    return result



if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        input_data = parse_input_lines([x.strip() for x in file.readlines()])

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 1 is:",
        f"{colorama.Fore.GREEN}{solve_1(input_data)}{colorama.Style.RESET_ALL} ===")

    # print(
    #     f"=== For \"{sys.argv[1]}\" the solution for part 2 is:",
    #     f"{colorama.Fore.GREEN}{solve_2(input_data)}{colorama.Style.RESET_ALL} ===")