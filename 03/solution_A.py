#!/usr/bin/env python

def is_sym(c):
    return c not in '.0123456789'


def is_symbol_adjacent(diagram, y, x):
    for y1 in range(y-1, y+2):
        for x1 in range(x-1, x+2):
            try:
                cell = diagram[y1][x1]
                if cell not in '.0123456789':
                    return True
            except IndexError:
                pass
    return False


with open('input.txt', 'r') as f:
    diagram = [ line.strip() for line in f ]

sum = 0

for y in range(len(diagram)):
    cur_num = None
    line = diagram[y]
    for x in range(len(line)):
        c = line[x]
        if c.isdigit():
            n = int(c)
            sym = is_symbol_adjacent(diagram, y, x)
            if cur_num is None:
                cur_num = [n, sym]
            else:
                cur_num[0] *= 10
                cur_num[0] += int(c)
                cur_num[1] = cur_num[1] or sym
        else:
            if cur_num is not None:
                n, adj = cur_num
                if adj:
                    sum += n
                    print("+", end="")
                print(f"{n}")
            cur_num = None
    if cur_num is not None:
        n, adj = cur_num
        if adj:
            sum += n
            print("+", end="")
        print(f"{n}")
print(f"Sum: {sum}")