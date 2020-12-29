import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from util import *

TILE_SIZE = 10  # width = height

Sides = cl.namedtuple('s', 'top bot lef ri')

def extent(img):
    rs = [r for (r, c) in img.keys()]
    cs = [c for (r, c) in img.keys()]
    return [range(min(rs), max(rs)+1), range(min(cs), max(cs)+1)]

def canon(line):
    try:
        line = ''.join(line)
        a = int(line.replace('#','1').replace('.','0'), 2)
        rev = ''.join(reversed(line))
        b = int(rev.replace('#','1').replace('.','0'), 2)
        # print('ok', line)
        if a > b:
            return line
        else:
            return rev
    except:
        print('failed', line)

def get_borders(lines, canonicalize=False):
    sides = [
        ''.join([lines[0][i] for i in range(10)]),
        ''.join([lines[9][i] for i in range(10)]),
        ''.join([lines[i][0] for i in range(10)]),
        ''.join([lines[i][9] for i in range(10)]),
    ]
    if canonicalize:
        sides = [canon(s) for s in sides]
    return Sides(*sides)

def orientations(lines):
    for i in range(4):
        lines = rotmat(lines)
        yield [''.join(l) for l in lines]
        yield [''.join(l) for l in fliphorz(lines)]
