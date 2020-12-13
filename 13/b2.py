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
rawbuses = findints(f.readline().strip())
# below line is example input. comment out to use the real input
rawbuses = [7,13,'x','x',59,'x',31,19]
goal = [i for i, b in enumerate(rawbuses) if b != 'x']
buses = [b for b in rawbuses if b != 'x']
t = 0
print('goal \t', goal)
scatters = [wait(b, t) for b in buses]
while True:
    if t % 10000 == 0:
        p(t, '\t', scatters)
    scatters = [wait(b, t) for b in buses]
    if goal == scatters:
        print(t)
        exit()
    t += buses[0]
