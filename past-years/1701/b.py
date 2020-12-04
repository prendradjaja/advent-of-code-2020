import fileinput, collections, collections as cl, itertools, math, random, sys, re
# from grid import gridsource as grid, make_grid_class # *, gridsource, gridcardinal, gridplane
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    f = open(sys.argv[1])
    for line in f:
        line = line.strip()
        break
    # line = '1111'
    tot = 0
    for i in range(len(line)):
        j = (i + len(line) // 2) % len(line)
        i, j = int(line[i]), int(line[j])
        if i == j:
            tot += i
    print(tot)

if __name__ == '__main__' and not sys.flags.inspect: main()
