"""
without orientation / flip

also doesn't count up the number of #s, just the number of monsters
"""

from util import consecutives
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
monsters = 0
for i, lines in enumerate(consecutives((l.strip() for l in f), 3)):
    ilines = interleave(lines)
    for m in regex.finditer(ilines):
        if m.start() % 3 == 0:
            monsters += 1
print(monsters)
