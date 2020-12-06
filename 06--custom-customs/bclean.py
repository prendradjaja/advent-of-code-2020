import sys

def intersection(first, *others):
    return set(first).intersection(*others)

f = open(sys.argv[1])
tot = 0
for line in f.read().split('\n\n'):
    people = [set(x) for x in line.split('\n')]
    tot += len(intersection(*people))
print(tot)
