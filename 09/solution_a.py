#!/usr/bin/env python

import sys


def predict(seq):
    is_terminal = bool(seq[0] == 0)
    subseq = []
    for i in range(1, len(seq)):
        subseq.append(seq[i] - seq[i-1])
        if seq[i] != 0:
            is_terminal = False

    if is_terminal:
        print(f"predict({seq}) = 0")
        return 0
    else:
        p = seq[-1] + predict(subseq)
        print(f"predict({seq}) = {p}")
        return p


def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append([int(x) for x in line.strip().split()])
    return data


def main(filename):
    data = read_data(filename)
    total = 0
    for s in data:
        print("-------------")
        p = predict(s)
        total += p
    print(f"Total: {total}")


if __name__ == '__main__':
    filename = sys.argv[1]
    main(filename)
