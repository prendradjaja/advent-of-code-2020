import fileinput, collections, itertools, math, random, sys, re
from grid import gridsource as grid, make_grid_class # *, gridsource, gridcardinal, gridplane
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    for line in fileinput.input():
        line = line.strip()
        break
    n = 0
    for i, c in enumerate(line):
        n += 1 if c == '(' else -1
        if n < 0:
            print(i+1)
            exit()
    print(n)

if __name__ == '__main__' and not sys.flags.inspect: main()