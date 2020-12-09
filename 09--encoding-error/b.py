import itertools, sys
from util import consecutives

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    x = 25
    nums = [int(line.strip()) for line in f]
    target = 731031916
    idxs = list(range(1000))
    for c in itertools.combinations(idxs, 2):
        a, b = c
        if sum(nums[a: b + 1]) == target:
            r = nums[a: b + 1]
            print(min(r) + max(r))

main()
