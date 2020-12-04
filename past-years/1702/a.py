import fileinput, collections, collections as cl, itertools, math, random, sys, re
# from grid import gridsource as grid, make_grid_class # *, gridsource, gridcardinal, gridplane
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    f = open(sys.argv[1])
    tot = 0
    for line in f:
        line = line.strip()
        nums = [int(x) for x in line.split('\t')]
        c = max(nums) - min(nums)
        tot+=c
    print(tot)

if __name__ == '__main__' and not sys.flags.inspect: main()
