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

    p1win, cards = combat(p1, p2)
    score = 0
    mult = 1
    for x in reversed(cards):
        score += mult * x
        mult += 1
    print(score)

def combat(p1, p2, depth=0):
    def freeze():
        return (tuple(p1), tuple(p2))
    seen = set()
    for i in itertools.count(start=1):
        # print('  ' * depth + f'Round {i}')
        # print('  ' * depth + f'P1 deck {p1}')
        # print('  ' * depth + f'P2 deck {p2}')
        if freeze() in seen:
            return True, p1
        seen.add(freeze())
        if len(p1) and len(p2):
            c1 = p1.pop(0)
            c2 = p2.pop(0)
            # print('  ' * depth + f'c1 {c1}')
            # print('  ' * depth + f'c2 {c2}')
            if len(p1) >= c1 and len(p2) >= c2:
                p1win, _ = combat(p1[:c1], p2[:c2], depth+1)
            else:
                p1win = c1 > c2
        else:
            p1win = bool(p1)
            return p1win, p1 if p1win else p2
        # print('  ' * depth + f'Player {2 - int(p1win)} wins this round')
        # print()
        if p1win:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
