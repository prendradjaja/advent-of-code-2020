import fileinput
from collections import defaultdict

def unitvec(d):
    if d == 'R':
        return [1, 0]
    elif d == 'D':
        return [0, 1]
    elif d == 'L':
        return [-1, 0]
    elif d == 'U':
        return [0, -1]

def addvec(v, w):
    return [v[0] + w[0], v[1] + w[1]]
seen = set()

dists = defaultdict(int)

[wire1, wire2] = [line for line in fileinput.input()]

pos = [0, 0]
dist = 0
for inst in wire1.split(','):
    d, *m = inst
    m = int(''.join(m))
    vec = unitvec(d)
    for i in range(m):
        dist += 1
        pos = addvec(pos, vec)
        seen.add(str(pos))
        dists[str(pos)] += dist

inters = []

pos = [0, 0]
dist = 0
for inst in wire2.split(','):
    d, *m = inst
    m = int(''.join(m))
    vec = unitvec(d)
    for i in range(m):
        dist += 1
        pos = addvec(pos, vec)
        if str(pos) in seen:
            inters.append(pos)
            dists[str(pos)] += dist

print(inters)

interdists = []

for loc in inters:
    x, y = loc
    interdists.append(dists[str(loc)])

print(interdists)
print(min(interdists))
