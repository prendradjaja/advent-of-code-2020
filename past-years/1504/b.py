import fileinput, collections, itertools, math, random, sys, re, hashlib
# from grid import gridsource as grid, make_grid_class # *, gridsource, gridcardinal, gridplane
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    puzin = 'ckczppom'
    i = 1
    while True:
        if hashlib.md5((puzin + str(i)).encode('utf-8')).hexdigest().startswith('0'*6):
            print(i)
            exit()
        i += 1

if __name__ == '__main__' and not sys.flags.inspect: main()
