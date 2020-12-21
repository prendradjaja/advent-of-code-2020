import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
# from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import one

Food = cl.namedtuple('f', 'ings allers')
# https://stackoverflow.com/a/2953343/1945088
def intersection(first, *others):
    return set(first).intersection(*others)


def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    foods = []
    for line in f:
        line = line.strip()
        left, right = line.split(' (contains ')
        right = right.replace(')', '').replace(',', '')
        left = left.split()
        right = right.split()
        foods.append(Food(left, right))
    atofind = set()
    for f in foods:
        for a in f.allers:
            atofind.add(a)
    itoa = {}
    atoi = {}
    changed = True
    while changed:
        changed = False
        for a in atofind:
            sets = []
            for f in foods:
                if a in f.allers:
                    sets.append(set(f.ings) - set(itoa))
            candidates = intersection(*sets)
            if len(candidates) == 1:
                itoa[one(candidates)] = a
                atoi[a] = one(candidates)
                atofind.remove(a)
                changed = True
                break

    ans = 0
    for f in foods:
        for x in set(f.ings) - set(itoa):
            ans += 1
    print('Part 1:', ans)

    res = []
    for a in sorted(atoi):
        res.append(atoi[a])
    print('Part 2:', ','.join(res))



main() # if __name__ == '__main__' and not sys.flags.inspect: main()
