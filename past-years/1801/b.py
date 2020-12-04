import fileinput, collections, itertools, math, random, sys, re
# from grid import gridsource as grid, make_grid_class # *, gridsource, gridcardinal, gridplane
verbose = False
# verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    tot = 0
    seen = set()
    f = [line.strip() for line in fileinput.input()]
    while True:
        for line in f:
            n = int(line)
            tot += n
            log(tot, seen)
            if tot in seen:
                print(tot)
                exit()
            seen.add(tot)

if __name__ == '__main__' and not sys.flags.inspect: main()
