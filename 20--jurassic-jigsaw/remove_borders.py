from helpers import *

def remove_borders(img):
    rs, cs = extent(img)
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
                    line += img[(r, c)]
        imglines.append(line)
    return imglines
