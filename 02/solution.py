#!/usr/bin/env python

import re

digits = [
    '0', 'one|1', 'two|2', 'three|3',
    'four|4', 'five|5', 'six|6',
    'seven|7', 'eight|8', 'nine|9'
]


def id_digit(s):
    global digits
    for i in range(len(digits)):
        if re.match(f"^{digits[i]}", s):
            return i
    return None


def find_digit(s, find_last=False):
    x = range(0, len(s), 1)
    if find_last:
        x = range(len(s), -1, -1)
    for i in x:
        d = id_digit(s[i:])
        if d is not None:
            return d
    return None


sum = 0

with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        first, last = (find_digit(line), find_digit(line, True))
        sum += first * 10 + last

print(f"Sum is {sum}")
