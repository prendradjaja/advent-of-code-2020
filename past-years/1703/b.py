import fileinput, collections, itertools, math, random
from grid import griddigital as grid
# *, gridnatural, gridcardinal, griddigital
verbose = False
# verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

x = 325489
# x = 3
pos = [0, 0]

g = collections.defaultdict(lambda: collections.defaultdict(int))

neivecs = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]


def spiral(n):
        k=math.ceil((math.sqrt(n)-1)/2)
        t=2*k+1
        m=t**2
        t=t-1
        if n>=m-t: return k-(m-n),-k
        else: m=m-t
        if n>=m-t: return -k,-k+(m-n)
        else: m=m-t
        if n>=m-t: return -k+(m-n),k
        else: return k,k-(m-n-t)

g[0][0] = 1

for i in range(2, x+1):
    pos = spiral(i)
    log(pos)
    nei = [grid.addvec(pos, n) for n in neivecs]
    log(nei)
    newval = list(grid.index(g, n) for n in nei)
    log(newval)
    newval = sum(newval)
    if newval > x:
        print(newval)
        exit()
    g[pos[0]][pos[1]] = newval
    log(newval)
    log()
