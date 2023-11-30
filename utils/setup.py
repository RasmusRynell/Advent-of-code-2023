import os
import sys
import requests

year = '2022'


def get_input(problem):
    url = 'https://adventofcode.com/' + year + '/day/' + problem + '/input'
    return requests.get(url, cookies={'session': os.environ['AOC_SESSION']}).text

if __name__ == '__main__':
    if len(sys.argv) > 1:
        problem = sys.argv[1]
        
    if len(sys.argv) > 2:
        override = sys.argv[2]

    if not os.path.exists('problems') or override:
        os.makedirs('problems', exist_ok=True)

    if not os.path.exists('problems/' + problem) or override:
        os.makedirs('problems/' + problem, exist_ok=True)

    if not os.path.exists('problems/' + problem + '/inputs') or override:
        os.makedirs('problems/' + problem + '/inputs', exist_ok=True)

    # Create a simple empty input file
    if not os.path.exists('problems/' + problem + '/inputs/simple_input.txt') or override:
        with open('problems/' + problem + '/inputs/simple_input.txt', 'w') as f:
            f.write('')

    if not os.path.exists('problems/' + problem + '/inputs/input.txt') or override :
        input_txt = get_input(problem)
        with open('problems/' + problem + '/inputs/input.txt', 'w') as f:
            f.write(input_txt)

    if not os.path.exists('problems/' + problem + '/main.py') or override:
        with open('problems/' + problem + '/main.py', 'w') as f:
            with open('utils/template.py', 'r') as template:
                f.write(template.read())

    if not os.path.exists('problems/' + problem + '/utils.py') or override:
        with open('problems/' + problem + '/utils.py', 'w') as f:
            with open('utils/utils.py', 'r') as template:
                f.write(template.read())
