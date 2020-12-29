from util import consecutives, fliphorz, rotmat
import fileinput
import re
import sys
from helpers import *

# Trailing whitespace inside the string is important!
monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.replace(' ', '.').split('\n')[1:]
MONSTER_HEIGHT = len(monster)

def find_monsters_and_roughness(lines):
    pattern = interleave(monster)
    regex = re.compile(pattern)

    for o in orientations(lines):
        # TODO This assumes that only one orientation has monsters
        found, painted = paintmons(o, regex)
        if found:
            roughness = 0
            for line in painted:
                for c in line:
                    if c == '#':
                        roughness += 1
            return roughness

def interleave(lines):
    """
    >>> interleave(["abc", "123"])
    'a1b2c3'
    """
    res = ''
    for chars in zip(*lines):
        res += ''.join(chars)
    return res

def paintmons(m, regex):
    monsters = 0
    newm = [list(line) for line in m]  # copy and turn lines into mutable lists
    for i, lines in enumerate(consecutives((l.strip() for l in m), MONSTER_HEIGHT)):
        ilines = interleave(lines)
        for match in regex.finditer(ilines):
            if match.start() % MONSTER_HEIGHT == 0:
                # monster found!
                monsters += 1

                # paint it
                for r, line in enumerate(monster):
                    for c, ch in enumerate(line):
                        if ch == '#':
                            y = r + i
                            x = c + (match.start() // MONSTER_HEIGHT)
                            # print( m[y][x] == '#')
                            assert m[y][x] == '#'
                            newm[y][x] = 'O'
    return monsters, newm
