import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

Tile = cl.namedtuple('t', 'tid lines')
Sides = cl.namedtuple('s', 'top bot lef ri')

ans = 63187742854073

def main():
    PART_1 = len(sys.argv) > 2 and sys.argv[2] == 'p1'
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    tiles = [parse(t) for t in f.read().split('\n\n')]
    tilesbybord = collections.defaultdict(set)
    for t in sorted(tiles):
        bs = borders(t.lines)
        for b in sorted(bs):
            tilesbybord[b].add(t.tid)
    # p(tilesbybord)

    def matches(t):
        bs = borders(t.lines)
        res = []
        for b in sorted(bs):
            res.extend(list(tilesbybord[b]))
        return set(res) - {t.tid}

    # first = True
    # while tiles:
    #     if first:
    #         t = tiles[0]
    #         tiles.remove(t)
    #     else:
    #         prev = t

    def getbyid(tid):
        return one([t for t in tiles if t.tid == tid])

    img = {}
    positions = {}  # by tid

    def orient(t, prev):
        match = one(borders(t) & borders(prev))

    def iterbord(prev, canonicalize):
        r, c = positions[prev.tid]
        if canonicalize:
            top = canon(''.join([img[(r, c+i)] for i in range(10)]))
            bot = canon(''.join([img[(r+9, c+i)] for i in range(10)]))
            lef = canon(''.join([img[(r+i, c)] for i in range(10)]))
            ri = canon(''.join([img[(r+i, c+9)] for i in range(10)]))
        else:
            top = (''.join([img[(r, c+i)] for i in range(10)]))
            bot = (''.join([img[(r+9, c+i)] for i in range(10)]))
            lef = (''.join([img[(r+i, c)] for i in range(10)]))
            ri = (''.join([img[(r+i, c+9)] for i in range(10)]))
        return Sides(top, bot, lef, ri)

    def iterunplaced(lines, canonicalize):
        r, c = (0, 0)
        if canonicalize:
            top = canon(''.join([lines[r][ c+i] for i in range(10)]))
            bot = canon(''.join([lines[r+9][ c+i] for i in range(10)]))
            lef = canon(''.join([lines[r+i][ c] for i in range(10)]))
            ri = canon(''.join([lines[r+i][ c+9] for i in range(10)]))
        else:
            top = (''.join([lines[r][ c+i] for i in range(10)]))
            bot = (''.join([lines[r+9][ c+i] for i in range(10)]))
            lef = (''.join([lines[r+i][ c] for i in range(10)]))
            ri = (''.join([lines[r+i][ c+9] for i in range(10)]))
        return Sides(top, bot, lef, ri)

    def revstr(line):
        return ''.join(reversed(line))

    def place(u, parent):
        # print('finding placement for', u)
        u = getbyid(u)
        parent = getbyid(parent)

        r, c = positions[parent.tid]

        ps = iterbord(parent, False)
        psc = iterbord(parent, True)
        us = iterunplaced(u.lines, False)
        usc = iterunplaced(u.lines, True)
        match = one(set(psc) & set(usc))

        # if match == psc.bot:
        #     if match == usc.top:
        #         pos = (r+10, c)
        #         res = u.lines
        #         if ps.bot != us.top:
        #             res = fliphorz(res)
        #     elif match == 
        #     else: raise Exception("To implement")
        # else: raise Exception("To implement")

        if match == psc.bot:
            pedge = ps.bot
            for lines in oris(u):
                uedge = iterunplaced(lines, False).top
                if uedge == pedge:
                    return (r+10, c), lines
        elif match == psc.ri:
            pedge = ps.ri
            for lines in oris(u):
                uedge = iterunplaced(lines, False).lef
                if uedge == pedge:
                    return (r, c+10), lines
        elif match == psc.top:
            pedge = ps.top
            for lines in oris(u):
                # bla = iterunplaced(lines, False)
                uedge = iterunplaced(lines, False).bot
                if uedge == pedge:
                    # print('top')
                    # print(uedge)
                    # print(pedge)
                    # print(bla)
                    return (r-10, c), lines
        elif match == psc.lef:
            pedge = ps.lef
            for lines in oris(u):
                uedge = iterunplaced(lines, False).ri
                if uedge == pedge:
                    return (r, c-10), lines
        else: raise Exception("impossible")
        return pos, lines

    def oris(m):
        lines = m.lines
        for i in range(4):
            lines = rotmat(lines)
            yield lines
            yield fliphorz(lines)



    visited = set()
    def dfs(u, parent=None):
        # (visit goes here)
        # p(u)
        if len(visited) == 0: # first tile
            t = getbyid(u)
            for r, row in enumerate(t.lines):
                for c, ch in enumerate(row):
                    img[(r, c)] = ch
            positions[u] = (0, 0)
            # print('placing first')
            # display()
            # print(iterbord(tiles[0]))
        else:
            pos, lines = place(u, parent)
            for r, row in enumerate(lines):
                for c, ch in enumerate(row):
                    img[grid.addvec(pos, (r, c))] = ch
            # print('placing', pos)
            # display()
            positions[u] = pos

        visited.add(u)
        for v in sorted(matches(getbyid(u))):
            if v not in visited:
                dfs(v, u)
    dfs(tiles[0].tid)

    rs, cs = extent(img)
    def getpix(r, c):
        if (r, c) in img:
            return img[(r, c)]
        else:
            return '?'

    if PART_1:
        ids = {pos: idnum for (idnum, pos) in positions.items()}
        rmin = min(rs)
        rmax = max(rs) - 9
        cmin = min(cs)
        cmax = max(cs) - 9
        rs2 = [rmin, rmax]
        cs2 = [cmin, cmax]
        res = 1
        for pos in itertools.product(rs2, cs2):
            res *= ids[pos]
        print(res)
    else:
        imglines = []
        for y, r in enumerate(rs):
            if y % 10 in [0, 9]:
                continue
            else:
                line = ''
                for x, c in enumerate(cs):
                    if x % 10 in [0, 9]:
                        pass
                    else:
                        line += getpix(r,c)
            imglines.append(line)
        for line in imglines:
            print(line)

def extent(img):
    rs = [r for (r, c) in img.keys()]
    cs = [c for (r, c) in img.keys()]
    return [range(min(rs), max(rs)+1), range(min(cs), max(cs)+1)]



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
