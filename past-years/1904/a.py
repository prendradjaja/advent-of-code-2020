import fileinput
from itertools import tee

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b, c = tee(iterable, 3)
    next(b, None)
    next(c, None)
    next(c, None)
    return zip(a, b, c)

pmin = 158126
pmax = 624574

# def twoadj(n):
#     prev = -1
#     for i in str(n):
#         i = int(i)
#         if i == prev:
#             return True
#         prev = i
#     return False

def twoadj(n):
    return 2 in rle(str(n))

def rle(s):
    prev = None
    res = []
    n = 0
    for c in s:
        if c == prev:
            n += 1
        else:
            res.append(n)
            n = 1
            prev = c
    res.append(n)
    return res

def nodec(n):
    prev = -1
    for i in str(n):
        i = int(i)
        if i < prev:
            return False
        prev = i
    return True

print(twoadj(112233))
print(twoadj(123444))
print(twoadj(111122))

count = 0

for n in range(pmin, pmax+1):
    if nodec(n) and  twoadj(n):
        count += 1

print(count)
