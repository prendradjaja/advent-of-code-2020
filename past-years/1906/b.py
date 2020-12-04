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
depths = {}
paths = {}

for line in fileinput.input():
    v, w = line.strip().split(')')
    tree[v].append(w)
    # parents[w] = v

def dfs(v, depth=1, path=''):
    for w in tree[v]:
        depths[w] = depth
        paths[w] = path+v+'/'
        dfs(w, depth+1, paths[w])

# won't return the correct answer if v is ancestor of w (or vice versa)
def commonancestor(v, w):
    pv = paths[v]
    pw = paths[w]
    path = ''
    for i in range(min(len(pv), len(pw))):
        if pv[i] == pw[i]:
            path += pv[i]
    return path.split('/')[-2]

orbits = 0
dfs('COM')
# print(depths)
# print(paths)
print(commonancestor('A', 'D'))
