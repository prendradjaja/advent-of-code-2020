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
    def valid(n, rule):
        return rule.lo1 <= n <= rule.hi1 or rule.lo2 <= n <= rule.hi2

    for tic in tix.split('\n'):
        tic = findints(tic.strip())
        invalid(tic)
    p(erate)




main() # if __name__ == '__main__' and not sys.flags.inspect: main()
