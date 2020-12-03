import fileinput
import re

num_valid = 0
total = 0

for line in fileinput.input():
    line = (line
        .strip()
        .replace('-', ' ')
        .replace(':', '')
    )
    mincount, maxcount, c, password = line.split()
    mincount = int(mincount)
    maxcount = int(maxcount)
    count = len(re.findall(c, password))
    if mincount <= count <= maxcount:
        num_valid += 1
    total += 1

print(f'{num_valid} of {total}')
