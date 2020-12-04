import fileinput
from math import prod

f = []

for line in fileinput.input():
    line = line.strip()
    f.append(line)
    width = len(line)

treenums = []

for r in [1, 3, 5, 7]:
    pos = -r
    trees = 0
    for line in f:
        pos = (pos + r) % width
        if line[pos] == '#':
            trees += 1
    treenums.append(trees)

pos = -1
trees = 0
for line in f[::2]:
    pos = (pos + 1) % width
    if line[pos] == '#':
        trees += 1
treenums.append(trees)

print(prod(treenums))
