import os
import sys
import requests
from aocd import get_data

year = '2023'


def get_input(day):
    TOKEN = os.getenv('AOC_SESSION')
    return get_data(TOKEN, day=int(day), year=int(year))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        day = sys.argv[1]
        
    override = False
    if len(sys.argv) > 2:
        override = sys.argv[2]
        

    if not os.path.exists('problems') or override:
        os.makedirs('problems', exist_ok=True)

    if not os.path.exists('problems/day_' + day) or override:
        os.makedirs('problems/day_' + day, exist_ok=True)

    if not os.path.exists('problems/day_' + day + '/inputs') or override:
        os.makedirs('problems/day_' + day + '/inputs', exist_ok=True)

    if not os.path.exists('problems/day_' + day + '/inputs/simple1.txt') or override:
        with open('problems/day_' + day + '/inputs/simple1.txt', 'w') as f:
            f.write('')

    if not os.path.exists('problems/day_' + day + '/inputs/simple2.txt') or override:
        with open('problems/day_' + day + '/inputs/simple2.txt', 'w') as f:
            f.write('')

    if not os.path.exists('problems/day_' + day + '/inputs/input.txt') or override :
        input_txt = get_input(day)
        with open('problems/day_' + day + '/inputs/input.txt', 'w') as f:
            f.write(input_txt)

    if not os.path.exists('problems/day_' + day + '/main.py') or override:
        with open('problems/day_' + day + '/main.py', 'w') as f:
            with open('utils/template.py', 'r') as template:
                f.write(template.read())
