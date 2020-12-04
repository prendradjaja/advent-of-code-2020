import fileinput, collections, itertools, math, random, sys, re
# from grid import gridsource as grid, make_grid_class # *, gridsource, gridcardinal, gridplane
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    for line in fileinput.input():
        line = line.strip()
        break
    w = 25
    h = 6
    layers = []
    while line:
        layer, line = line[:w*h], line[w*h:]
        layers.append(layer)
    fewest = min(layers, key=count(0))
    print (count(1)(fewest) * count(2)(fewest))

def count(n):
    def c(s):
        return len([c for c in s if c == str(n)])
    return c

if __name__ == '__main__' and not sys.flags.inspect: main()
