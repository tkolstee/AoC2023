#!/usr/bin/env python3

import sys
import os
import re

path = ['seed', 'soil', 'fertilizer', 'water', 'light',
        'temperature', 'humidity', 'location'
]


def resolve_map(map, input):
    for entry in map:
        dest_start, src_start, rng = entry
        src_pos = input - src_start
        if src_pos >= 0 and src_pos < rng:
            return dest_start + src_pos
    return input


def get_cmdline():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} filename")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print(f"Input file {filename} not found.")
        sys.exit(1)

    return filename


def read_data(filename):
    maps = {}
    seeds = []
    cur_map = None
    with open(filename, 'r') as f:
        for line in f:
            line.strip()

            if re.match('^\s*$', line):
                continue

            m = re.match('\s*seeds:\s*(\d.*\d)\s*', line)
            if m:
                seeds = [ int(x) for x in re.split('\s+', m.group(1)) ]

            m = re.match('\s*(\S+)-to-(\S+)\smap:\s*', line)
            if m:
                cur_map = (m.group(1), m.group(2))
                maps[cur_map] = []
            
            m = re.match('\s*(\d+)\s+(\d+)\s+(\d+)\s*', line)
            if m:
                if cur_map is None:
                    print(f"Numbers with no map: '{line}'")
                    sys.exit(1)
                maps[cur_map].append( tuple([int(x) for x in m.groups()]) )
    return seeds, maps


def resolve_seed(seed, maps):
    loc = seed
    print(f"Seed: {loc}", end="")
    for i in range(1, len(path)):
        have = path[i-1]
        need = path[i]
        the_map = maps[(have, need)]
        loc = resolve_map(the_map, loc)
        print(f" -> {need}: {loc}", end="")
    print("")
    return loc


def main():
    filename = get_cmdline()
    seeds, maps = read_data(filename)
    locs = [ resolve_seed(seed, maps) for seed in seeds ]
    print(locs)
    print(f"MIN: {min(locs)}")



if __name__ == '__main__':
    main()

