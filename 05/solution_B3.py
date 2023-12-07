#!/usr/bin/env python3

import sys
import re

path = [ 'seed', 'soil', 'fertilizer', 'water', 'light', 
        'temperature', 'humidity', 'location' ]
seeds = []
maps = {}


def range_from_len(start, len):
    return range(start, start+len)


def read_data(filename):
    global seeds, maps
    with open(filename, 'r') as f:
        seedlist = [ int(x) for x in f.readline().split()[1:] ]
        for i in range(0, len(seedlist), 2):
            seeds.append(range(seedlist[i], seedlist[i]+seedlist[i+1]))

        srctype = dsttype = None
        for line in f:
            line = line.strip()
            m = re.match(r'(\w+)-to-(\w+) map:', line)
            if m:
                srctype = m.group(1)
                dsttype = m.group(2)
                maps[(srctype,dsttype)] = []
                maps[(dsttype,srctype)] = []

            m = re.match('(\d+)\s+(\d+)\s+(\d+)', line)
            if m:
                dststart, srcstart, rangelen = [ int(x) for x in m.groups() ]
                srcrange = range(srcstart, srcstart+rangelen)
                dstrange = range(dststart, dststart+rangelen)
                srcoff = srcstart - dststart
                dstoff = dststart - srcstart

                maps[(srctype, dsttype)].append((srcrange, dstoff))
                maps[(dsttype, srctype)].append((dstrange, srcoff))


def lookup_map(srctype, dsttype, srcnum, identity=True):
    map = maps[(srctype, dsttype)]
    for entry in map:
        rng, off = entry
        if srcnum in rng:
            newval = srcnum + off
            return newval
    if identity:
        return srcnum
    else:
        raise KeyError


def trace_seed(seed):
    result = seed
    for i in range(1, len(path)):
        result = lookup_map(path[i-1], path[i], result)
    return result


def trace_loc(loc, identity=True):
    result = loc
    for i in range(len(path)-1, 0, -1):
        result = lookup_map(path[i], path[i-1], result, identity=identity)
    return result


def main():
    filename = sys.argv[1]
    read_data(filename)

    map = maps[('location', 'humidity')]
    lowest_loc = None
    for entry in map:
        entry_start = entry[0][0]
        if lowest_loc is None or lowest_loc > entry_start:
            lowest_loc = entry_start
    seed = trace_loc(lowest_loc, identity=False)
    print(f"Lowest loc: {seed}")

    # for seedrange in seeds:
    #     for seed in seedrange:
    #         loc = trace_seed(seed)
    #         backtoseed = trace_loc(loc)
    #         if lowest is None or loc < lowest:
    #             lowest = loc
    #             print(f"New winner: {seed} => {loc} => {backtoseed}")


if __name__ == '__main__':
    main()

