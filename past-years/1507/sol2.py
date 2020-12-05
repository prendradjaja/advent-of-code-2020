import fileinput, collections, collections as cl, itertools, math, random, sys, re
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

f = open(sys.argv[1])
lines = []
for line in f:
    line = (
        line
        .replace('AND', '&')
        .replace('OR', '|')
        .replace('LSHIFT', '<<')
        .replace('RSHIFT', '>>')
        .replace('NOT', '65535 -')
    )
    lines.append(line)

while lines:
    for line in lines[:]:
        try:
            exec(line)
            lines.remove(line)
            # print(line)
        except NameError:
            pass
print(var_a)
