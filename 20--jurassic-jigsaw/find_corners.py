from helpers import *

def find_corners(img, positions):
    rs, cs = extent(img)
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
    return res
