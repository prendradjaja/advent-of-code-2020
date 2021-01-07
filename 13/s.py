import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    f = [line.strip() for line in f]
    start, buses = f
    start = int(start)
    buses = '7,13,x,x,59,x,31,19'
    buses = [(i, int(x)) for i, x in enumerate(buses.split(',')) if x != 'x']
    # buses = [int(x) for x in buses.split(',') if x != 'x']
    # times = {}
    # for b in buses:
    #     i = start + 1
    #     while True:
    #         if i % b == 0:
    #             times[b] = i
    #             break
    #         i += 1
    # p(times[min(times, key=lambda b: times[b])] - start)
    def earliest(b, start):
        return b - (start % b)
    i = 0
    goal = [i for i, b in buses]
    print(goal)
    while True:
        if i % 1000 == 0:
            p(i)
        scatters = []
        for n, b in buses:
            scatters.append(earliest(b, i))
        if scatters == goal:
            print(i)
            return
        # p(scatters, i)
        # print(i, scatters)
        # input()

        i += buses[0][1]

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
