import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
# from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

Rule = cl.namedtuple('r', 'lo1 hi1 lo2 hi2')

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    rulesstr, mine, tix = f.read().split('\n\n')
    rules = []
    for r in rulesstr.split('\n'):
        r = r.strip()
        r = r.replace('-', ' ')
        rules.append(Rule(*findints(r)))
    erate = 0
    def invalid(tic):
        nonlocal erate
        for n in tic:
            if all(not valid(n, r) for r in rules):
                erate += n
                return True
        return False
    def valid(n, rule):
        return rule.lo1 <= n <= rule.hi1 or rule.lo2 <= n <= rule.hi2
    def validrules(n):
        res = []
        for i, r in enumerate(rules):
            if valid(n, r):
                res.append(i)
        return set(res)

    valids = []
    for tic in tix.split('\n'):
        tic = findints(tic.strip())
        if not invalid(tic):
            valids.append(tic)
    valids = valids[1:]

    numfields = len(valids[0])
    numrules = len(rules)
    candsbyidx = {i: set(range(numrules)) for i in range(numfields)}
    for tic in valids:
        for i, n in enumerate(tic):
            candsbyidx[i] = candsbyidx[i].intersection(validrules(n))

    idxbyfld = {}

    while candsbyidx:
        idx = sorted(candsbyidx, key=lambda x: len(candsbyidx[x]))[0]
        fld = one(candsbyidx[idx])
        idxbyfld[fld] = idx
        del candsbyidx[idx]
        for s in candsbyidx.values():
            if fld in s:
                s.remove(fld)

    mine = ints(mine.split('\n')[1].strip().split(','))
    res = 1
    for i in range(6):
        idx = idxbyfld[i]
        res *= mine[idx]
    p(res)

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
