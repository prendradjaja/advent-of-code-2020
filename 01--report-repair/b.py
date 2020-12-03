import fileinput
from itertools import combinations
from math import prod

entries = [int(line) for line in fileinput.input()]

# O(n^3)
for triple in combinations(entries, 3):
    if sum(triple) == 2020:
        print(f'Product of {triple} = {prod(triple)}')
        exit()

print('No 2020 triple found.')
