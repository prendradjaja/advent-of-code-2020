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
    for i in range(len(line)):  # initially had +1
        j = i - 1
        i = i % len(line)  # not needed -- artifact of +1
        i, j = int(line[i]), int(line[j])
        if i == j:
            tot += i
    print(tot)

if __name__ == '__main__' and not sys.flags.inspect: main()
