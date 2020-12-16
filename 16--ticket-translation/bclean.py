import sys, collections
from util import findints

Rule = collections.namedtuple('r', 'lo1 hi1 lo2 hi2')

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

    # During the competition, I didn't fix the bug in the commented-out code
    # below. Instead, I printed out candsbyidx and manually figured out the
    # field indices.
    for x in candsbyidx:
        print(x, candsbyidx[x])

    # def done():
    #     return all(len(item) == 1 for item in candsbyidx.values())
    # while not done():
    #     for x in candsbyidx:
    #         if len(candsbyidx[x]) == 1:
    #             torem = one(candsbyidx[x])
    #             for s in candsbyidx.values():
    #                 if torem in s:
    #                     p('removing')
    #                     s.remove(torem)
    # for x in candsbyidx:
    #     p(x, candsbyidx[x])

main()
