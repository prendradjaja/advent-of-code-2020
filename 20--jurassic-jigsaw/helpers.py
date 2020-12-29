import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from util import *

Sides = cl.namedtuple('s', 'top bot lef ri')

Tile = cl.namedtuple('t', 'tid lines')
def extent(img):
    rs = [r for (r, c) in img.keys()]
    cs = [c for (r, c) in img.keys()]
    return [range(min(rs), max(rs)+1), range(min(cs), max(cs)+1)]

def parse(t):
    n, *lines = [x for x in t.strip().split('\n')]
    n = findint(n)
    return Tile(n, lines)

def get_tile(tid, tiles):
    return one([t for t in tiles if t.tid == tid])

def topbotbords(lines):
    return set([canon(lines[0]), canon(lines[-1])])

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


def subimage(img, rows, cols):
    """
    Does a little bit more than it says on the tin: Also converts from coord-keyed dict to list of rows
    """
    res = []
    for r in rows:
        line = ''
        for c in cols:
            line += img[(r, c)]
        res.append(line)
    return res

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

def get_neighbors(tid, tiles, tids_by_border):
    tile = get_tile(tid, tiles)
    bs = get_borders(tile.lines, True)
    res = []
    for b in sorted(bs):
        res.extend(list(tids_by_border[b]))
    return set(res) - {tile.tid}

def orientations(lines):
    for i in range(4):
        lines = rotmat(lines)
        yield [''.join(l) for l in lines]
        yield [''.join(l) for l in fliphorz(lines)]
