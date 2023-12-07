#!/usr/bin/env python3

import sys
import os
import re

path = ['seed', 'soil', 'fertilizer', 'water', 'light',
        'temperature', 'humidity', 'location'
]


def resolve_map(map, input, reverse=False, return_orig_on_unfound=True):
    for entry in map:
        if reverse:
            src_start, dest_start, rng = entry
        else:
            dest_start, src_start, rng = entry

        src_pos = input - src_start
        if src_pos >= 0 and src_pos < rng:
            return dest_start + src_pos
    if return_orig_on_unfound:
        return input
    else:
        raise RuntimeError


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
    for i in range(1, len(path)):
        have = path[i-1]
        need = path[i]
        the_map = maps[(have, need)]
        loc = resolve_map(the_map, loc)
    return loc


def resolve_loc(loc, maps):
    seed = loc
    print(f"Loc: {loc}", end="")
    for i in range(len(path)-1, 0, -1):
        have = path[i]
        need = path[i-1]
        the_map = maps[(need, have)]
        mirror_lookup = (i < (len(path)-1) and i > 0)
        seed = resolve_map(the_map, seed, reverse=True, return_orig_on_unfound=mirror_lookup)
        print(f" -> {need} ({seed}) ", end="")
    print("")
    return seed


def main():
    filename = get_cmdline()
    seeds, maps = read_data(filename)
    seed = None
    i = 1
    while seed is None:
        try:
            seed = resolve_loc(i, maps)
        except RuntimeError:
            pass
        i += 1
    
    print(seed)



    # seed_ranges = []
    # for i in range(0, len(seeds), 2):
    #     seed_ranges = ()


    # locs = []
    # for i in range(0, len(seeds), 2):
    #     start = seeds[i]
    #     rng = seeds[i+1]
    #     end = start + rng - 1
    #     for seed in range(start, end):
    #         locs.append(resolve_seed(seed, maps))

    # print(locs)
    # print(f"MIN: {min(locs)}")



if __name__ == '__main__':
    main()

