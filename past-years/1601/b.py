import fileinput
import collections
import itertools
import math
import random

verbose = False
verbose = True

def log(*args, **kwargs):
    if verbose:
        print(*args, **kwargs)

for line in fileinput.input():
    steps = line.strip().split(', ')
    break

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d = dirs[0]
pos = [0, 0]
seen = set()

def add(a, b):
    return [x+y for x,y in zip(a,b)]

def updatedir(c):
    global d
    if c == 'R':
        d = dirs[(dirs.index(d) + 1) % 4]
    elif c == 'L':
        d = dirs[(dirs.index(d) - 1) % 4]
    else:
        1/0

for step in steps:
    c, *n = step
    n = int(''.join(n))
    updatedir(c)
    for i in range(n):
        pos = add(pos, d)
        sp = str(pos)
        if sp in seen:
            print(sum(abs(x) for x in eval(sp)))
            exit()
        seen.add(sp)

