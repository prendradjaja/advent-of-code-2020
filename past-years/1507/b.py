import fileinput, collections, collections as cl, itertools, math, random, sys, re
from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *
verbose = False
verbose = True
def log(*args, **kwargs):
    if verbose: print(*args, **kwargs)

def main():
    f = open(sys.argv[1])
    wires = [line.strip() for line in f]
    values = {None: None}
    while wires:
        for w in wires[:]:
            l, r = w.split(' -> ')
            cmd = None
            if 'AND' in l:
                a, b = l.split(' AND ')
            elif 'OR' in l:
                a, b = l.split(' OR ')
            elif 'LSHIFT' in l:
                a, n = l.split(' LSHIFT ')
                b = None
            elif 'RSHIFT' in l:
                a, n = l.split(' RSHIFT ')
                b = None
            elif 'NOT' in l:
                a = l.split('NOT ')[1]
                b = None
            else:
                try:
                    n = int(l)
                    a, b = None, None
                    cmd = 'LITERAL'
                except ValueError:
                    a = l
                    b = None
                    cmd = 'DIRECT'
            if a in values and b in values:
                print('remove', w, len(wires))
                wires.remove(w)
                if 'AND' in l:
                    values[r] = values[a] & values[b]
                elif 'OR' in l:
                    values[r] = values[a] | values[b]
                elif 'LSHIFT' in l:
                    values[r] = values[a] << int(n)
                elif 'RSHIFT' in l:
                    values[r] = values[a] >> int(n)
                elif 'NOT' in l:
                    values[r] = 65535 - values[a]
                elif cmd == 'LITERAL':
                    values[r] = int(n)
                elif cmd == 'DIRECT':
                    values[r] = values[a]
                else:
                    1/0
    print(values)
    print(values['a'])




if __name__ == '__main__' and not sys.flags.inspect: main()
