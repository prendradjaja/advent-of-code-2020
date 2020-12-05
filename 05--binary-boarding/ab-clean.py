import sys

def main():
    f = open(sys.argv[1])
    sids = []
    for line in f:
        line = line.strip()
        sid = decode(line)
        sids.append(sid)
    print('Part 1:', max(sids))
    prev = min(sids) - 1
    for sid in sorted(sids):
        if sid != prev + 1:
            print('Part 2:', sid - 1)
            return
        prev = sid

def decode(line):
    rows = list(range(128))
    cols = list(range(8))
    for c in line:
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
        sid = row * 8 + col
    return sid

main()
