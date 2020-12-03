import fileinput
import collections
import itertools
import math
import random

verbose = False
verbose = True

def log(*args, **kwargs):
    if verbose:
        print(*args, **kwargs)

tree = collections.defaultdict(list)

for line in fileinput.input():
    v, w = line.strip().split(')')
    tree[v].append(w)

def dfs(v, depth=1):
    global orbits
    for w in tree[v]:
        orbits += depth
        dfs(w, depth+1)

orbits = 0
dfs('COM')
print(orbits)
