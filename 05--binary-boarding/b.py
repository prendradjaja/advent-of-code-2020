import fileinput, collections, collections as cl, itertools, math, random, sys, re
# from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
# from util import *
verbose = False
# verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    # print(decode('BFFFBBFRRR'))
    # exit()
    f = open(sys.argv[1])
    sids = []
    for line in f:
        line = line.strip()
        sid = decode(line)
        sids.append(sid)
    prev = min(sids) - 1
    for sid in sorted(sids):
        print(sid)
        # if sid != prev + 1:
        #     print(sid)
        # prev = sid
    # print(max(sids))

def decode(line):
    rows = list(range(128))
    cols = list(range(8))
    for i, c in enumerate(line):
        if c == 'F':
            rows = rows[:len(rows)//2]
        elif c == 'B':
            rows = rows[len(rows)//2:]
        elif c == 'L':
            cols = cols[:len(cols)//2]
        elif c == 'R':
            cols = cols[len(cols)//2:]
        row = rows[0]
        col = cols[0]
        log(i, c, row, col, rows, cols)
        sid = row * 8 + col
    return sid


if __name__ == '__main__' and not sys.flags.inspect: main()
