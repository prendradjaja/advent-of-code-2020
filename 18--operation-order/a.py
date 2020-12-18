import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
# from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import ints

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    results = []
    def ev(line):
        if '(' not in line:
            mode = None
            for c in line:
                if isinstance(c, int):
                    if not mode:
                        val = int(c)
                    else:
                        val = eval(f'{val} {mode} {int(c)}')
                elif c == '+':
                    mode = c
                elif c == '*':
                    mode = c
                else:
                    1/0
            return val
        else:
            oi = lastindex(line, '(')
            ci = line[oi:].index(')') + oi
            subex = line[oi+1:ci]
            subval = ev(subex)
            return ev(line[:oi] + [subval] + line[ci+1:])

    def lastindex(seq, item):
        res = None
        for i, e in enumerate(seq):
            if e == item:
                res = i
        return res

    for line in f:
        line = line.strip()
        line = line.replace(' ', '')
        line = ints(list(line))
        results.append(ev(line))
    print(sum(results))


main() # if __name__ == '__main__' and not sys.flags.inspect: main()
