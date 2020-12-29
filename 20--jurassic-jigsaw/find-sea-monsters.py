"""
without orientation / flip

also doesn't count up the number of #s, just the number of monsters
"""

from util import consecutives, fliphorz, rotmat
import re
import sys

monster = """
                  #
#    ##    ##    ###
 #  #  #  #  #  #""".replace(' ', '.').split('\n')[1:]

def interleave(lines):
    """
    >>> interleave(["abc", "123"])
    'a1b2c3'
    """
    res = ''
    for chars in zip(*lines):
        res += ''.join(chars)
    return res

pattern = interleave(monster)
regex = re.compile(pattern)


f = open(sys.argv[1] if len(sys.argv) > 1 else 'monsterinput')
lines = [l.strip() for l in f.readlines()]

def bigoris(m):
    lines = m
    for i in range(4):
        lines = rotmat(lines)
        yield [''.join(l) for l in lines]
        yield [''.join(l) for l in fliphorz(lines)]

def countmons(m):
    monsters = 0
    for i, lines in enumerate(consecutives((l.strip() for l in m), 3)):
        ilines = interleave(lines)
        for m in regex.finditer(ilines):
            if m.start() % 3 == 0:
                monsters += 1
    return monsters

for o in bigoris(lines):
    c = countmons(o)
    # print(c)
    if c:
        pass
        print(c)
        print(o)

