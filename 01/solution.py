#!/usr/bin/env python

sum = 0

with open('input.txt', 'r') as f:
  for line in f:
    for c in line[:]:
      if c.isdigit():
        sum += int(c) * 10
        break
    for c in line[::-1]:
      if c.isdigit():
        sum += int(c)
        break

print(f"Sum is {sum}")