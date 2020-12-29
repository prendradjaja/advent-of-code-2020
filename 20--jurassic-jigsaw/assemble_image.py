import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
from helpers import *

def assemble_image(tiles, tids_by_border):
    # { [(row, col)]: '#' or '.' }
    img = {}

    # top left corner position of each placed tile
    # { [tid]: (row, col) }
    positions = {}

    # tids of visited tiles
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

            positions[u] = pos

        visit()
        visited.add(u)  # We could just use `positions` as `visited`, but using a separate visited set makes the DFS structure clearer

        for v in sorted(get_neighbors(u, tiles, tids_by_border)):
            if v not in visited:
                dfs(v, u)

    dfs(tiles[0].tid)

    return img, positions

def get_placement(u, parent, tiles, positions, img):  #TODO requires a lot of state passed around!
    """
    Determine where to place the new tile

    u: tid of new tile
    parent: tid of the previously-placed tile ("parent" in DFS) that this new tile will be adjacent to
    """
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
