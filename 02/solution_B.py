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
    power = 1
    for v in result.values():
        power *= v
    return power


gamefile = sys.argv[1]
powersum = 0
with open(gamefile, 'r') as f:
    for line in f:
        m = re.match('^Game (\d+)\s*:\s*(.*)\s*$', line)
        if not m:
            continue
        game_num = int(m.group(1))
        power = process_game(m.group(2))
        powersum += power
print(f"Result: {powersum}")
