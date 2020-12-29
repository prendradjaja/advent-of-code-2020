from helpers import *

def find_corners(img, positions):
    rext, cext = extent(img)
    rs = (min(rext), max(rext) - TILE_SIZE + 1)
    cs = (min(cext), max(cext) - TILE_SIZE + 1)

    tids = {pos: tid for (tid, pos) in positions.items()}
    res = 1
    for pos in itertools.product(rs, cs):
        res *= tids[pos]
    return res
