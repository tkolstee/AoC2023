#!/usr/bin/env python

import sys
import math


def read_data(filename):
    race_data = []
    with open(filename, 'r') as f:
        time = [int(x) for x in f.readline().split()[1:]]
        dist = [int(x) for x in f.readline().split()[1:]]
    for i in range(len(time)):
        race_data.append((time[i], dist[i]))
    return race_data


def ways_to_win(time, dist):
    print(f"---------------------------Race: Time {time}, dist {dist}")
    # Distance traveled forms a parabola of form -x^2 + tx - d
    # Where t is the total time of the race
    #       x is the hold time
    #       d is the winning distance
    # If we find the vertex and one of the zero crossings,
    # The "ways to win" will be double the distance between them.
    v = time / 2
    
    # Make sure there's any way to win at all, vertex > 0
    vy = ((time ** 2) / 4) - dist
    if vy <= 0:
        return 0

    # Find X value of lower root
    z = (time - math.sqrt((time**2)-(4*dist))) / 2


    # Find length of positive portion (2 * dist(z-v))
    l = abs(v - z) * 2

    wins = math.floor(l)

    # Fractional portion
    frac_z = z - math.floor(z)
    frac_l = l - math.floor(l)
    frac_sum = frac_z + frac_l
    if frac_sum == 0:
        wins -= 1
    elif frac_sum > 1:
        wins += 1

    print(f"Game - time {time} dist {dist}: vertex: ({v}, {vy}), lower root: {z}, length: {l}, wins: {wins}")

    return max(0, wins)


def main(filename):
    race_data = read_data(filename)
    ways = [ways_to_win(*race) for race in race_data]
    total = 1
    for x in ways:
        total *= x
    print(total)


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
