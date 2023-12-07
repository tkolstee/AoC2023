#!/usr/bin/env python

import sys
import re

colors = ['red', 'green', 'blue']


def process_game(round):
    entry_re = re.compile(r'\d+\s+[a-z]+\b')
    result = {}
    for color in colors:
        result[color] = 0
    m = re.findall(entry_re, round)
    for i in m:
        num, color = re.split('\s+', i)
        if result[color] < int(num):
            result[color] = int(num)
    return result


def is_poss(game_result, available_cubes):
    for color in colors:
        if game_result[color] > available_cubes[color]:
            return False
    return True

gamefile = sys.argv[1]
avail = {}
for color in colors:
    x = int(input(f"How many {color} cubes? "))
    avail[color] = x

gamesum = 0
with open(gamefile, 'r') as f:
    for line in f:
        m = re.match('^Game (\d+)\s*:\s*(.*)\s*$', line)
        if not m:
            continue
        game_num = int(m.group(1))
        result = process_game(m.group(2))
        poss = is_poss(result, avail)
        print(f"Game {game_num}: {poss}")
        if poss:
            gamesum += game_num
print(f"Result: {gamesum}")
