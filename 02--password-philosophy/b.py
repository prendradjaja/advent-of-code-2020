import fileinput
import re

def valid(pos1, pos2, c, password):
    """
    >>> valid(1, 3, 'a', 'abcde')
    True
    >>> valid(1, 3, 'b', 'cdefg')
    False
    >>> valid(2, 9, 'c', 'ccccccccc')
    False
    """
    positions = [pos1, pos2]
    num_matches = 0
    for pos in positions:
        num_matches += password[pos - 1] == c
    return num_matches == 1

num_valid = 0
total = 0

for line in fileinput.input():
    line = (line
        .strip()
        .replace('-', ' ')
        .replace(':', '')
    )
    pos1, pos2, c, password = line.split()
    pos1 = int(pos1)
    pos2 = int(pos2)
    if valid(pos1, pos2, c, password):
        num_valid += 1
    total += 1

print(f'{num_valid} of {total}')
