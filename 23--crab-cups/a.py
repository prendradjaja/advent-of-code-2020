import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

# notes for optimizing for part 2
# ################# = copy basically the entire array -- probably super slow
# #### = iterate over the array -- possibly slow

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    cups = ints(list('716892543'))
    # cups = ints(list('389125467'))

    for m in range(100):
        pick = cups[1:4]
        cups = [cups[0]] + cups[4:] ######################
        cur = cups[0]
        destl = cur
        while destl in (pick + [cur]):
            destl -= 1
            if destl == 0:
                destl = 9
        desti = cups.index(destl) + 1 #####
        cups = cups[:desti] + pick + cups[desti:] ######################
        cups = rot(cups) ######################
    onei = cups.index(1) ###
    for _ in range(onei + 1):
        cups = rot(cups) ######################
    print(''.join(str(x) for x in cups[:-1]))

def rot(lst):
    return lst[1:] + [lst[0]]

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
