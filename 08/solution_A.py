#!/usr/bin/python

import sys
import re


def read_data(filename):
    node_re = re.compile(r'^([A-Z]{3}) = \(([A-Z]{3}), ([A-Z]{3})\)')
    with open(filename, 'r') as f:
        directions = f.readline().strip()
        nodes = {}
        for line in f:
            m = re.match(node_re, line)
            if m:
                nodes[m.group(1)] = tuple([m.group(2), m.group(3)])
    return directions, nodes


def follow(directions, nodes, pos, goal):
    steps = 0
    dirs = 'LR'
    for d in directions:
        pos = nodes[pos][dirs.index(d)]
        print(".", end="")
        steps += 1
        if pos == goal:
            return True, steps, pos
    return False, steps, pos


def main(filename):
    directions, nodes = read_data(filename)
    steps = 0
    iterations = 0
    pos = 'AAA'
    goal = 'ZZZ'
    while True:
        iterations += 1
        print(f"Iteration {iterations} ({steps} steps so far): ", end="")
        success, new_steps, pos = follow(directions, nodes, pos, goal)
        print("")
        steps += new_steps
        if success:
            break
    print(f"Final totals: Iterations {iterations}, steps {steps}")


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
