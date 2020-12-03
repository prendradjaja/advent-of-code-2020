import fileinput
import collections
import itertools
import math
import random

from grid import dirsdigital as dirs

verbose = False
verbose = True

k = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

pos = [1, 1]

def addvec(a, b):
    return [max(min(x+y, 2), 0) for x,y in zip(a,b)]

def log(*args, **kwargs):
    if verbose:
        print(*args, **kwargs)

for line in fileinput.input():
    line = line.strip()
    for c in line:
        v = dirs.tovec[c]
        pos = addvec(pos, v)
    print(k[pos[0]][pos[1]], end='')
print()
