import itertools, sys
from util import consecutives

def main():
    f = open(sys.argv[1] if len(sys.argv) > 1 else 'in')
    x = 25
    nums = [int(line.strip()) for line in f]
    def valid(a, b):
        for c in itertools.combinations(a, 2):
            if c[0] + c[1] == b:
                return True
        return False
    for i, seq in enumerate(consecutives(nums, x + 1)):
        a = seq[:x]
        b = seq[-1]
        if not valid(a, b):
            print(b)

main()
