import sys
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
                else: 1/0
            newval = int(newval, 2)
            mem[idx] = newval
        else: 1/0
    p(sum(mem.values()))

main()
