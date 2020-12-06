import sys

f = open(sys.argv[1])
tot = 0
for line in f.read().split('\n\n'):
    tot += len(set(line.strip().replace('\n','')))
print(tot)
