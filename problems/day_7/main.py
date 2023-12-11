import os
import sys
import time
import colorama
from pathlib import Path
import functools
from collections import Counter

# fmt: off
sys.path.append(str(Path(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))).parent / 'utils/'))
from utils import time_function, average_time_function
# fmt: on

char_value_order = ['A', 'K', 'Q', 'J', 'T',
                    '9', '8', '7', '6', '5', '4', '3', '2']
char_value_order_part2 = ['A', 'K', 'Q', 'T',
                          '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def compare_hands(hand1_in, hand2_in):
    # If 1 < 2, return -1 # Hand 2 is better
    # If 1 = 2, return 0 # Tie
    # If 1 > 2, return 1 # Hand 1 is better

    hand1_best, hand1_second_best = calculate_hand_value(hand1_in[0])
    hand2_best, hand2_second_best = calculate_hand_value(hand2_in[0])

    if hand1_best > hand2_best:  # hand 1 is better
        return 1
    elif hand1_best < hand2_best:  # hand 2 is better
        return -1

    if hand1_second_best > hand2_second_best:  # hand 1 is better
        return 1
    elif hand1_second_best < hand2_second_best:  # hand 2 is better
        return -1

    for card in zip(hand1_in[0], hand2_in[0]):
        # Hand 1 better
        if char_value_order.index(card[0]) < char_value_order.index(card[1]):
            return 1
        elif char_value_order.index(card[0]) > char_value_order.index(card[1]):
            return -1


def calculate_hand_value(hand, use_jokers=False):
    hand_count = Counter(hand)

    jokers = hand_count['J'] if use_jokers else 0
    if jokers >= 4 and use_jokers:
        return 5, 0
    if use_jokers:
        del hand_count['J']

    sorted_hand_count = sorted(
        hand_count.items(), key=lambda item: item[1], reverse=True)

    best_hand_card_count = sorted_hand_count[0][1] if sorted_hand_count else 0
    second_best_hand_card_count = sorted_hand_count[1][1] if len(
        sorted_hand_count) > 1 else 0

    return best_hand_card_count + jokers, second_best_hand_card_count


def compare_hands_2(hand1_in, hand2_in):
    # If 1 < 2, return -1 # Hand 2 is better
    # If 1 = 2, return 0 # Tie
    # If 1 > 2, return 1 # Hand 1 is better

    hand1_best, hand1_second_best = calculate_hand_value(hand1_in[0], True)
    hand2_best, hand2_second_best = calculate_hand_value(hand2_in[0], True)

    if hand1_best > hand2_best:  # hand 1 is better
        return 1
    elif hand1_best < hand2_best:  # hand 2 is better
        return -1

    if hand1_second_best > hand2_second_best:  # hand 1 is better
        return 1
    elif hand1_second_best < hand2_second_best:  # hand 2 is better
        return -1

    for card in zip(hand1_in[0], hand2_in[0]):
        # Hand 1 better
        if char_value_order_part2.index(card[0]) < char_value_order_part2.index(card[1]):
            return 1
        elif char_value_order_part2.index(card[0]) > char_value_order_part2.index(card[1]):
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
    key_func = functools.cmp_to_key(compare_hands_2)
    result = sorted(input_data, key=key_func)

    res = 0
    for i in range(len(result)):
        res += (i+1)*int(result[i][1])

    return res


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

    print(
        f"=== For \"{sys.argv[1]}\" the solution for part 2 is:",
        f"{colorama.Fore.GREEN}{solve_2(input_data)}{colorama.Style.RESET_ALL} ===")
