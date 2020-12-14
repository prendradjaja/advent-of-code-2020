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
            bidx = f"{idx:036b}"
            newidx = ''
            for m, n in zip(mask, bidx):
                if m == 'X':
                    newidx += 'X'
                elif m == '0':
                    newidx += n
                elif m == '1':
                    newidx += '1'
                else:
                    print('invalid', m)
                    1/0
            _newidx = newidx
            # newidx = int(newidx, 2)
            xs = len([c for c in _newidx if c == 'X'])
            for i in range(2**xs):
                myidx = newidx
                bits = f"{i:b}".rjust(xs, '0')
                for b in bits:
                    myidx = myidx.replace('X', b, 1)
                try:
                    mem[int(myidx, 2)] = val
                except ValueError:
                    print(myidx)
                    print(newidx, xs)
                    exit()
        else: 1/0
    p(sum(mem.values()))

main() # if __name__ == '__main__' and not sys.flags.inspect: main()

