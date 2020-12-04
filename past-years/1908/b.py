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
    # w = 2
    # h = 2
    # line = '0222112222120000'
    layers = []
    while line:
        layer, line = line[:w*h], line[w*h:]
        layers.append(layer)

    # fewest = min(layers, key=count(0))
    # print (count(1)(fewest) * count(2)(fewest))

    img = collections.defaultdict(dict)
    # any of these work -- all i need is the above, though
    # img = collections.defaultdict(lambda: collections.defaultdict(str))
    # img = collections.defaultdict(lambda: collections.defaultdict(int))
    for r in range(h):
        for c in range(w):
            for layer in layers:
                pixel = layer[r * h + c]
                if pixel == str(0):
                    img[r][c] = '#'
                    break
                if pixel == str(1):
                    img[r][c] = '.'
                    break

    # log(img[0])
    for r in range(h):
        print(''.join(img[r][c] for c in range(w)))


def count(n):
    def c(s):
        return len([c for c in s if c == str(n)])
    return c

if __name__ == '__main__' and not sys.flags.inspect: main()
