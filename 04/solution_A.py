#!/usr/bin/env python

import re
from collections import defaultdict

cardline = re.compile('^Card\s+(\d+):\s+(\d.*\d)\s+\|\s+(\d.*\d)\s+$')
points = 0

with open('input.txt', 'r') as f:
    for line in f:
        m = re.match(cardline, line)
        if not m:
            continue
        cardnum = m.group(1)
        winning = set(re.split('\s+', m.group(2)))
        mine = set(re.split('\s+', m.group(3)))
        matches = mine.intersection(winning)
        num_matches = len(matches)
        pts = 0
        if num_matches > 0:
            pts = 2 ** (num_matches-1)
        
        
        print(f"Card {cardnum}: {num_matches} matches for {pts} points: ({matches})")

        points += pts
    
print(f"Total: {points} points")
