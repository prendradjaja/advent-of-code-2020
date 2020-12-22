import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
# from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
# from util import *

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    p1, p2 = f.read().split('\n\n')
    def parse(p):
        return [int(x.strip()) for x in p.split('\n')[1:]]
    p1 = parse(p1)
    p2 = parse(p2)
    while bool(p1) and bool(p2):
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])
    mult = 1
    score = 0
    cards = p1 + p2
    for x in reversed(cards):
        score += mult * x
        mult += 1
    print(score)

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
