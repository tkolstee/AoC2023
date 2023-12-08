#!/usr/bin/env python

import sys
import re

def rng_intersect(a, b):
    """
    Returns a 3-element array: before, overlap, after.
    Overlap is a range of common elements between A and B.
    Before and after represent elements in A not in B.
    Ranges for which no values exist are replaced by None.    
    """
    if not (isinstance(a, range) and isinstance(b, range)):
        raise ValueError("Both inputs must be ranges.")
    if not (a.step == 1 and b.step == 1):
        raise ValueError("Both input ranges must have step=1.")

    before = None
    after = None
    overlap = None

    if b.start >= a.stop:   # No overlap, all in "before"
        before = a
    elif b.stop <= a.start: # No overlap, all in "after"
        after = a
    elif a.start >= b.start and a.stop <= b.stop:  # All-overlap
        overlap = a
    else:
        overlap = range( max(a.start, b.start), min(a.stop, b.stop) )

        if b.start > a.start:
            before = range(a.start, b.start)

        if b.stop < a.stop:
            after = range(b.stop, a.stop)

    return [before, overlap, after]

def main(filename):
    with open(filename, 'r') as f:
        ranges = []
        seedranges = [int(x) for x in f.readline().strip().split()[1:] ]
        for i in range(0, len(seedranges), 2):
            start = seedranges[i]
            end = start + seedranges[i+1]
            ranges.append(range(start, end))
        ranges.sort(key=lambda x: x.stop)
        
        new_ranges = []
        for line in f:
            line.strip()

            if 'map' in line:
                ranges += new_ranges
                ranges.sort(key=lambda x: x.start)
                #print(ranges)
                new_ranges = []
                #print("------------------------------")
                print(f"{len(ranges)} ranges")
                print("------"+line.upper())


            m = re.match('^(\d+)\s+(\d+)\s+(\d+)$', line)
            if m:
                #print(f"-- Applying filter: {line}")
                dststart, srcstart, rngsize = [ int(x) for x in m.groups() ]
                xlate = range(srcstart, srcstart + rngsize)
                add_op = dststart - srcstart
                kept_ranges = []
                for rng in ranges:
                    #print(f"  -- RANGE: {rng}")
                    before, overlap, after = rng_intersect(rng, xlate)
                    if before is not None:
                        #print(f"    -- KEEP: {before.start}-{before.stop}")
                        kept_ranges.append(before)
                    if after is not None:
                        #print(f"    -- KEEP: {after.start}-{after.stop}")
                        kept_ranges.append(after)
                    if overlap is not None:
                        newrange = range(overlap.start+add_op, overlap.stop+add_op)
                        #print(f"    -- NEW: {overlap.start}-{overlap.stop} -> {newrange.start}-{newrange.stop}")
                        new_ranges.append(newrange)
                ranges = kept_ranges[:]
                #print(f"  -- After Filter: {ranges} {new_ranges}")


        ranges += new_ranges
        ranges.sort(key=lambda x: x.start)
        #print(ranges)
        new_ranges = []
        print("------------------------------")
        print(f"{len(ranges)} ranges")
        ranges.sort(key=lambda x: x.start)

        #print(ranges)
        print(f"Lowest value: {ranges[0].start}")

if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)