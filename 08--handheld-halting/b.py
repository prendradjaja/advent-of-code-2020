import fileinput, collections, collections as cl, itertools, math, random, sys, re, string
# from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
from util import *

Cmd = cl.namedtuple('c', 'which n')

def mutations(prog):
    for i in range(len(prog)):
        if prog[i].which == 'jmp':
            p = prog[:]
            p[i] = Cmd('nop', p[i][1])
            yield p
        elif prog[i].which == 'nop':
            p = prog[:]
            p[i] = Cmd('jmp', p[i][1])
            yield p

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    prog = []
    def terminates(prog):
        ip = 0
        acc = 0
        seen = set()
        while ip < len(prog):
            if ip in seen:
                return (False,)
            seen.add(ip)
            cmd = prog[ip]
            if cmd.which == 'jmp':
                ip += cmd.n
                pass
            elif cmd.which == 'acc':
                acc += cmd.n
                ip += 1
                pass
            elif cmd.which == 'nop':
                ip += 1
                pass
            else: 1/0
        return (True, acc)

    for line in f:
        line = line.strip()
        cmd = Cmd(*ints(line.split()))
        prog.append(cmd)

    p2('hi')
    for p in mutations(prog):
        res = terminates(p)
        if res[0]:
            print(res[1])

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
