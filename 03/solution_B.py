#!/usr/bin/env python

def find_num(line, i):
    if not line[i].isdigit():
        return None, None

    while line[i].isdigit() and i >= 0:
        i -= 1

    i += 1
    idx = i
    num = 0

    while i < len(line) and line[i].isdigit():
        num *= 10
        num += int(line[i])
        i += 1
    
    return idx, num


def find_adj(diagram, y, x):
    results = set()
    for y1 in range(y-1, y+2):
        for x1 in range(x-1, x+2):
            if y1 >= 0 and y1 < len(diagram) and x1 >= 0 and x1 <= len(diagram[y]):
                r = find_num(diagram[y1], x1)
                if r[0] is not None:
                    results.add((y1, r[0], r[1]))
    return results


def find_gear_ratio(diagram, y, x):
    results = find_adj(diagram, y, x)
    if len(results) == 2:
        res = [ x[2] for x in results ]
        a, b = res
        print(f"{a} * {b} = {a*b}")
        return a*b
    else:
        print(f"non-gear at {y}, {x}: {results}")
        return 0





with open('input.txt', 'r') as f:
    diagram = [ line.strip() for line in f ]

sum = 0

for y in range(len(diagram)):
    line = diagram[y]
    for x in range(len(line)):
        if line[x] == '*':
            sum += find_gear_ratio(diagram, y, x)

print(f"Final sum is {sum}")


