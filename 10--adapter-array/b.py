import collections
from util import consecutives
from functools import cache
import sys


def main():
    global ALL_JOLTAGES
    text = open(sys.argv[1] if len(sys.argv) > 1 else 'in').read()
    joltages = [int(n) for n in text.strip().splitlines()]
    joltages.append(0)
    joltages.append(max(joltages) + 3)
    joltages.sort()
    ALL_JOLTAGES = tuple(joltages)

    print(paths_to_max(0))


@cache
def paths_to_max(j):
    if j == ALL_JOLTAGES[-1]:
        return 1
    result = 0
    for k in successors(j):
        result += paths_to_max(k)
    return result


@cache
def successors(j):
    return tuple(k for k in ALL_JOLTAGES if k - j in [1, 2, 3])


if __name__ == '__main__':
    main()
