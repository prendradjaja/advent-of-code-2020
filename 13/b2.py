"""
I don't think brute force is possible for this problem, since
product(buses) is huge
"""

import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *


def wait(bid, start):
    if start % bid == 0:
        return 0
    return bid - (start % bid)

f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
_ = int(f.readline().strip())
rawbuses = ints(f.readline().strip().split(','), 'str')
foo = [(b, i) for i, b in enumerate(rawbuses) if b != 'x']
goal = [i for i, b in enumerate(rawbuses) if b != 'x']
buses = [b for b in rawbuses if b != 'x']
biggest = max(foo)
t = biggest[1]
print('goal \t', goal)
scatters = [wait(b, t) for b in buses]
while True:
    if t % 10000 == 0:
        p(t, '\t', scatters)
    scatters = [wait(b, t) for b in buses]
    if goal == scatters:
        print(t)
        exit()
    t += biggest[0]

# wait, is there a bug bc 'wait' is written assuming all buses start at 0? if so why does my code work anyway ughhhh
