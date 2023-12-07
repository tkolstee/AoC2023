#!/usr/bin/env python

import re
from collections import defaultdict

cardline = re.compile('^Card\s+(\d+):\s+(\d.*\d)\s+\|\s+(\d.*\d)\s+$')
copies = defaultdict(lambda: 1)
total = 1

with open('input.txt', 'r') as f:
    for line in f:
        m = re.match(cardline, line)
        if not m:
            continue
        cardnum = int(m.group(1))
        instances = copies[cardnum]
        if instances == 0:
            break

        winning = set(re.split('\s+', m.group(2)))
        mine = set(re.split('\s+', m.group(3)))
        num_matches = len(mine.intersection(winning))
        print(f"Card {cardnum}: {instances} instances, {num_matches} matches.")

        for i in range(cardnum+1, cardnum+1+num_matches):
            print(f"  -- you won {instances} copies of card {i}!")
            copies[i] += instances

print(copies)
num_cards = sum(copies.values())
print(f"Total: {num_cards}")