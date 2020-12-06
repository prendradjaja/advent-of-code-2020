import fileinput, collections, collections as cl, itertools, math, random, sys, re, string
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    valids = []
    for line in f:
        line = line.strip()
        line = line.replace('[','-')
        line = line.replace(']','')
        *letters, sid, csum = line.split('-')
        sid = int(sid)
        letters = ''.join(letters)
        cts = cl.Counter(letters)
        if getsum(cts) == csum:
            valids.append(sid)
            print(sid, caesar(letters, sid))
    valids
    print(sum(valids))


def getsum(cts):
    return ''.join([k for k in sorted(cts, key=lambda k: (-cts[k], k))][:5])

def caesar(s, n):
    return ''.join(caesarc(c, n) for c in s)

def caesarc(c, n):
    i = string.ascii_lowercase.find(c)
    return string.ascii_lowercase[(i + n) % 26]

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
