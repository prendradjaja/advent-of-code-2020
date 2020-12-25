import fileinput, collections, collections as cl, itertools, math, random, sys, re, string, functools
# from grid import gridsource as grid, gridcustom # *, gridsource, gridcardinal, gridplane
# from util import *

# Real input

cpub = 16616892
dpub = 14505727

# Example input

# cpub = 5764801
# dpub = 17807724

# DISCRETE LOGARITHM (log in modular arithmetic)
# calculator: https://www.alpertron.com.ar/DILOG.HTM
# more about the concept: https://en.wikipedia.org/wiki/Discrete_logarithm#Modular_arithmetic
#
# How to use the calculator to get the answer:
# base = 7 (sn)
# power = 16616892 (cpub)
# modulus = 20201227
# Find exp such that 7exp ≡ 16 616892 (mod 20 201227)
# exp = **16 243648** + 20 201226k
# x = the starred part
# foo(dpub, x) is the answer

def main():
    print(foo(dpub, 16_243648))  # See explanation above
    return

    # Brute force approach. This should be correct, but should take too long.

    # for i in itertools.count(start=0):
    #     tryc = foo(7, i)
    #     tryd = foo(7, i)
    #     if tryc == cpub:
    #         print(i)
    #         print(foo(dpub, i))
    #         return
    #     if tryd == dpub:
    #         print(i)
    #         print(foo(cpub, i))
    #         return

def foo(sn, LOOP_SIZE):
    x = 1
    for _ in range(LOOP_SIZE):
        x = x * sn
        x = x % 20201227
    return x

main() # if __name__ == '__main__' and not sys.flags.inspect: main()
