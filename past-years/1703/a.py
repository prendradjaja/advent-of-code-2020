import fileinput, collections, itertools, math, random
from grid import griddigital as grid
# *, gridnatural, gridcardinal, griddigital
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

x = 325489
# pos = [0, 0]gcco

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
# end
# p = (spiral(x))
# print (grid.absmanhattan(p))
print(spiral(1))
print(spiral(2))
print(spiral(3))

