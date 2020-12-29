import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
from helpers import *

Sides = cl.namedtuple('s', 'top bot lef ri')

ans = 63187742854073

def subimage(img, rows, cols):
    # res = []
    # for row in m[startrow:endrow]:
    #     res.append(row[startcol:endcol])
    # return res
    res = []
    for r in rows:
        line = ''
        for c in cols:
            line += img[(r, c)]
        res.append(line)
    return res

def get_borders(lines, canonicalize):
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

def get_neighbors(tile, tids_by_border):
    bs = borders(tile.lines)
    res = []
    for b in sorted(bs):
        res.extend(list(tids_by_border[b]))
    return set(res) - {tile.tid}

def borders(lines):
    # horz = topbotbords(lines)
    # vert = topbotbords(transpose(lines))
    # return horz | vert
    return list(get_borders(lines, True))

def main():
    PART_1 = len(sys.argv) > 2 and sys.argv[2] == 'p1'
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    tiles = [parse(t) for t in f.read().split('\n\n')]
    tids_by_border = collections.defaultdict(set)
    for t in sorted(tiles):
        bs = borders(t.lines)
        for b in sorted(bs):
            tids_by_border[b].add(t.tid)

    img = {}
    positions = {}  # by tid

    def orient(t, prev):
        match = one(borders(t) & borders(prev))

    def iterbord(prev, canonicalize):
        r, c = positions[prev.tid]
        lines = subimage(img, range(r, r + 10), range(c, c + 10))
        res = get_borders(lines, canonicalize)
        return res

    def place(u, parent):
        # print('finding placement for', u)
        u = get_tile(u, tiles)
        parent = get_tile(parent, tiles)

        r, c = positions[parent.tid]

        ps = iterbord(parent, False)
        psc = iterbord(parent, True)
        us = get_borders(u.lines, False)
        usc = get_borders(u.lines, True)
        match = one(set(psc) & set(usc))

        if match == psc.bot:
            pedge = ps.bot
            for lines in oris(u):
                uedge = get_borders(lines, False).top
                if uedge == pedge:
                    return (r+10, c), lines
        elif match == psc.ri:
            pedge = ps.ri
            for lines in oris(u):
                uedge = get_borders(lines, False).lef
                if uedge == pedge:
                    return (r, c+10), lines
        elif match == psc.top:
            pedge = ps.top
            for lines in oris(u):
                # bla = get_borders(lines, False)
                uedge = get_borders(lines, False).bot
                if uedge == pedge:
                    # print('top')
                    # print(uedge)
                    # print(pedge)
                    # print(bla)
                    return (r-10, c), lines
        elif match == psc.lef:
            pedge = ps.lef
            for lines in oris(u):
                uedge = get_borders(lines, False).ri
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
            t = get_tile(u, tiles)
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
        for v in sorted(get_neighbors(get_tile(u, tiles), tids_by_border)):
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
        print(res == ans)
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

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
