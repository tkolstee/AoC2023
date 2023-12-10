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


def predict_reverse(seq):
    is_terminal = bool(seq[0] == 0)
    subseq = []
    for i in range(1, len(seq)):
        subseq.append(seq[i] - seq[i-1])
        if seq[i] != 0:
            is_terminal = False

    if is_terminal:
        print(f"predict_reverse [ 0 ] {seq}")
        return 0
    else:
        p = predict_reverse(subseq)
        x = seq[0] - p
        print(f"predict_reverse [{x}] {seq}")
        return x


def read_data(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append([int(x) for x in line.strip().split()])
    return data


def main(filename, solution_B=False):
    data = read_data(filename)
    total = 0
    for s in data:
        if solution_B:
            p = predict_reverse(s)
        else:
            p = predict(s)
        total += p
    print(f"Total: {total}")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        main(filename)
    elif len(sys.argv) > 2 and sys.argv[2] == 'B':
        filename = sys.argv[1]
        main(filename, True)
    else:
        print(f"Usage:\n{sys.argv[0]} infile    - Solution A\n{sys.argv[0]} infile B  - Solution B")
