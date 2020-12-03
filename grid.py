dirslist = [[0, 1], [1, 0], [0, -1], [-1, 0]]

dirscardinal = {
    E: [0, 1],
    N: [1, 0],
    W: [0, -1],
    S: [-1, 0]
}

dirsnatural = {
    R: [0, 1],
    U: [1, 0],
    L: [0, -1],
    D: [-1, 0]
}

def dirtocardinal(d):
    for key in dirscardinal:
        if dirscardinal[key] == d:
            return key
    raise Exception("no cardinal direction found for " + str(d))

def dirtonatural(d):
    for key in dirsnatural:
        if dirsnatural[key] == d:
            return key
    raise Exception("no natural direction found for " + str(d))

def rotdir(direction, rotation):
    if rotation == R:
        return dirslist[(dirslist.index(d) + 1) % 4]
    elif rotation == L:
        return dirslist[(dirslist.index(d) - 1) % 4]
    else:
        raise Exception("invalid rotation direction: " + rotation)
