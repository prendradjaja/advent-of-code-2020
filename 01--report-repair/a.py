import fileinput
from itertools import combinations

entries = [int(line) for line in fileinput.input()]

# O(n^2)
for (a, b) in combinations(entries, 2):
    if a + b == 2020:
        print(f'{a} * {b} = {a * b}')
        exit()

print('No 2020 pair found.')
