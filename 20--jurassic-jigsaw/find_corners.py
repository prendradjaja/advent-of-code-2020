from helpers import *

def find_corners(img, positions):
    rext, cext = extent(img)
    rs = (min(rext), max(rext) - 9)
    cs = (min(cext), max(cext) - 9)

    tids = {pos: tid for (tid, pos) in positions.items()}
    res = 1
    for pos in itertools.product(rs, cs):
        res *= tids[pos]
    return res
