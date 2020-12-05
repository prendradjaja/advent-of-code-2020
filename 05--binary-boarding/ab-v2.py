import sys, re

f = open(sys.argv[1])
sids = []
for line in f:
    line =    re.sub(r'[FL]', '0', line.strip())
    sid = int(re.sub(r'[BR]', '1', line), 2)
    sids.append(sid)
print('Part 1:', max(sids))

sids = sorted(sids)
for a, b in zip(sids, sids[1:]):
    if b != a + 1:
        print('Part 2:', b - 1)
