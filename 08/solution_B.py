#!/usr/bin/python

import sys
import re
from ProgressDot import ProgressDot


class Directions:
    """ 
    Iterable that provides never-ending loops of the directions,
    and keeps track of calls (steps).
    """
    def __init__(self, dir_str):
        self.dirs = dir_str
        self.steps = 0

    def __iter__(self):
        self.steps = 0
        return self

    def __next__(self):
        i = self.steps % len(self.dirs)
        self.steps += 1
        return self.dirs[i]


def steps_to_z(pos, nodes, directions):
    dirs = Directions(directions)
    for dir in dirs:
        path = 'LR'.index(dir)
        pos = nodes[pos][path]
        if pos.endswith('Z'):
            return dirs.steps


def read_data(filename):
    node_re = re.compile(r'^(\w{3}) = \((\w{3}), (\w{3})\)')
    with open(filename, 'r') as f:
        directions = f.readline().strip()
        nodes = {}
        for line in f:
            m = re.match(node_re, line)
            if m:
                node, left, right = m.groups()
                nodes[node] = tuple([left, right])
    return directions, nodes


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(arr):
    if len(arr) == 1:
        return arr[0]
    
    a, b = arr[0:2]
    lcm_a_b = int((a / gcd(a, b)) * b)
    return lcm([ lcm_a_b ] + arr[2:])


def main(filename):
    dirs, nodes = read_data(filename)
    ghosts = []
    for n in nodes.keys():
        if n.endswith('A'):
            print(f"Checking on ghost at {n}...", end="")
            steps = steps_to_z(n, nodes, dirs)
            print(f"done. {steps}")
            ghosts.append(steps)
    print(lcm(ghosts))


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
