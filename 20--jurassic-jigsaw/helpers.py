import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from util import *

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

