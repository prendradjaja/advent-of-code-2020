import sys, collections
from util import *

Cmd = collections.namedtuple('c', 'which n')

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    prog = []
    for line in f:
        line = line.strip()
        cmd = Cmd(*ints(line.split()))
        prog.append(cmd)
    ip = 0
    acc = 0
    seen = set()
    while True:
        if ip in seen:
            print(acc)
            return
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

main()
