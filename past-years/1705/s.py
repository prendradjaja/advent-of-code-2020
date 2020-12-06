import fileinput, collections, collections as cl, itertools, math, random, sys, re
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    maze = [int(line.strip()) for line in f]
    p = 0
    i = 0
    while 0 <= p < len(maze):
        n = maze[p] + p
        if maze[p] >= 3:
            maze[p] -= 1
        else:
            maze[p] += 1
        p = n
        i += 1
    print(i)



main() # if __name__ == '__main__' and not sys.flags.inspect: main()
