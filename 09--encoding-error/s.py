import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    x = 25
    nums = [int(line.strip()) for line in f]
    # def valid(a, b):
    #     for c in itertools.combinations(a, 2):
    #         if c[0] + c[1] == b:
    #             return True
    #     return False
    # for i, seq in enumerate(consecutives(nums, x + 1)):
    #     a = seq[:x]
    #     b = seq[-1]
    #     if not valid(a, b):
    #         print(b)
    target = 731031916
    idxs = list(range(1000))
    for c in itertools.combinations(idxs, 2):
        a, b = c
        if sum(nums[a: b + 1]) == target:
            r = nums[a: b + 1]
            print(min(r) + max(r))

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
