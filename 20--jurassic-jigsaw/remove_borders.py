from helpers import *

def remove_borders(img):
    rs, cs = extent(img)
    imglines = []
    for y, r in enumerate(rs):
        if y % TILE_SIZE in [0, TILE_SIZE - 1]:
            continue
        else:
            line = ''
            for x, c in enumerate(cs):
                if x % TILE_SIZE in [0, TILE_SIZE - 1]:
                    pass
                else:
                    line += img[(r, c)]
        imglines.append(line)
    return imglines
