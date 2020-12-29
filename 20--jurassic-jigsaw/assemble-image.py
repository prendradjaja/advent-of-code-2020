import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
from helpers import *

ans = 63187742854073
def main():
    PART_1 = len(sys.argv) > 2 and sys.argv[2] == 'p1'
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    tiles = [parse(t) for t in f.read().split('\n\n')]
    tids_by_border = collections.defaultdict(set)
    for t in sorted(tiles):
        bs = get_borders(t.lines, True)
        for b in sorted(bs):
            tids_by_border[b].add(t.tid)

    img = {}
    positions = {}  # by tid




    visited = set()

    def dfs(u, parent=None):
        def visit():
            # Determine this tile's placement
            if not parent:
                pos = (0, 0)
                lines = get_tile(u, tiles).lines
            else:
                pos, lines = get_placement(u, parent, tiles, positions, img)

            # Place this tile
            for r, row in enumerate(lines):
                for c, ch in enumerate(row):
                    img[grid.addvec(pos, (r, c))] = ch

            # Store the placement of this tile's top-left corner (to be used by future get_placement calls in future visits)
            positions[u] = pos

        visit()
        visited.add(u)  # We could just use `positions` as `visited`, but using a separate visited set makes the DFS structure clearer

        for v in sorted(get_neighbors(u, tiles, tids_by_border)):
            if v not in visited:
                dfs(v, u)

    dfs(tiles[0].tid)

    rs, cs = extent(img)
    def getpix(r, c):
        if (r, c) in img:
            return img[(r, c)]
        else:
            1/0
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

def get_placement(u, parent, tiles, positions, img):  #TODO requires a lot of state passed around!
    u = get_tile(u, tiles)
    parent = get_tile(parent, tiles)
    r, c = positions[parent.tid]
    parent_lines = subimage(img, range(r, r + 10), range(c, c + 10))

    ps = get_borders(parent_lines, False)
    psc = get_borders(parent_lines, True)
    us = get_borders(u.lines)
    usc = get_borders(u.lines,True)
    match = one(set(psc) & set(usc))

    if match == psc.bot:
        pedge = ps.bot
        for lines in orientations(u.lines):
            uedge = get_borders(lines).top
            if uedge == pedge:
                return (r+10, c), lines
    elif match == psc.ri:
        pedge = ps.ri
        for lines in orientations(u.lines):
            uedge = get_borders(lines).lef
            if uedge == pedge:
                return (r, c+10), lines
    elif match == psc.top:
        pedge = ps.top
        for lines in orientations(u.lines):
            uedge = get_borders(lines).bot
            if uedge == pedge:
                return (r-10, c), lines
    elif match == psc.lef:
        pedge = ps.lef
        for lines in orientations(u.lines):
            uedge = get_borders(lines).ri
            if uedge == pedge:
                return (r, c-10), lines
    else: raise Exception("impossible")
    return pos, lines

def orientations(lines):
    for i in range(4):
        lines = rotmat(lines)
        yield lines
        yield fliphorz(lines)

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
