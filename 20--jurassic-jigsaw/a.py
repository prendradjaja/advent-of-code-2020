import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
# from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import findint, transpose, p

Tile = cl.namedtuple('t', 'tid lines')

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    tiles = [parse(t) for t in f.read().split('\n\n')]
    tilesbybord = collections.defaultdict(set)
    for t in tiles:
        bs = borders(t.lines)
        for b in bs:
            tilesbybord[b].add(t.tid)
    # p(tilesbybord)

    def matches(t):
        bs = borders(t.lines)
        res = []
        for b in bs:
            res.extend(list(tilesbybord[b]))
        return set(res) - {t.tid}

    for t in tiles:
        # p(t.tid, matches(t))
        p(t.tid, len(matches(t)))
        # Did the rest with Vim


def parse(t):
    n, *lines = [x for x in t.strip().split('\n')]
    n = findint(n)
    return Tile(n, lines)

def borders(lines):
    horz = topbotbords(lines)
    vert = topbotbords(transpose(lines))
    return horz | vert

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

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
