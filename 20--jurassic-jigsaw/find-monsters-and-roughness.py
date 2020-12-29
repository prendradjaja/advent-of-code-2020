from util import consecutives, fliphorz, rotmat
import fileinput
import re
import sys

monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """.replace(' ', '.').split('\n')[1:]

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


# f = open(sys.argv[1])
# # f = open(sys.argv[1] if len(sys.argv) > 1 else 'monsterinput')
# lines = [l.strip() for l in f.readlines()]
lines = []
for line in fileinput.input():
    lines.append(line.strip())

def bigoris(m):
    lines = m
    for i in range(4):
        lines = rotmat(lines)
        yield [''.join(l) for l in lines]
        yield [''.join(l) for l in fliphorz(lines)]

def paintmons(m):
    monsters = 0
    newm = [list(line) for line in m]  # copy and turn lines into mutable lists
    for i, lines in enumerate(consecutives((l.strip() for l in m), 3)):
        ilines = interleave(lines)
        for match in regex.finditer(ilines):
            if match.start() % 3 == 0:
                # monster found!
                monsters += 1

                # paint it
                for r, line in enumerate(monster):
                    for c, ch in enumerate(line):
                        if ch == '#':
                            y = r + i
                            x = c + (match.start() // 3)
                            # print( m[y][x] == '#')
                            assert m[y][x] == '#'
                            newm[y][x] = 'O'

    return monsters, newm

for o in bigoris(lines):
    found, painted = paintmons(o)
    if found:
        roughness = 0
        for line in painted:
            for c in line:
                if c == '#':
                    roughness += 1
        print(roughness)
        break
