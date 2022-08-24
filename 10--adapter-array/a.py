import collections
from util import consecutives
import sys


def main():
    text = open(sys.argv[1] if len(sys.argv) > 1 else 'in').read()
    joltages = [int(n) for n in text.strip().splitlines()]
    joltages.append(0)
    joltages.append(max(joltages) + 3)
    joltages.sort()

    difference_counts = collections.Counter()
    for a, b in consecutives(joltages):
        diff = b - a
        difference_counts[diff] += 1

    ones = difference_counts[1]
    threes = difference_counts[3]

    answer = ones * threes
    print(answer)


if __name__ == '__main__':
    main()
