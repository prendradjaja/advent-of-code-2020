import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
# from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    mem = {}
    for line in f:
        if 'mask' in line:
            mask = line.split(' = ')[1]
        elif 'mem' in line:
            idx, val = findints(line)
            bval = f"{val:036b}"
            newval = ''
            for m, n in zip(mask, bval):
                if m == 'X':
                    newval += n
                elif m in '01':
                    newval += m
                else:
                    print('invalid', m)
                    1/0
            newval = int(newval, 2)
            mem[idx] = newval
        else: 1/0
    p(sum(mem.values()))

main() # if __name__ == '__main__' and not sys.flags.inspect: main()

