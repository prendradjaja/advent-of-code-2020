import re

def tee_disableable(*args, **kwargs):
    print(*args, **kwargs) ############### can disable me by commenting out this line
    if args:
        return args[0]
p2 = tee_disableable

def tee(*args, **kwargs):
    print(*args, **kwargs)
    if args:
        return args[0]
p = tee

def pfirst(*args, **kwargs):
    if not pfirst.called:
        pfirst.called = True
        print(*args, **kwargs)
    return args[0]
pfirst.called = False
pf = pfirst

def ints(strings, mixedstring='error'):
    """
    Parses a sequence of strings, some of which are ints. Usually, each should be either exactly
    a number or contain no digits at all. In these cases, just return the string or int.

    If a "mixed string" (contains digits and nondigits) is
    encountered, then the `mixedstring` param determines the behavior:

    - 'error' (default)
    - 'str': keep it as a string
    - 'int': take just the int part

    Example:
    >>> s = "red 1 2"
    >>> color, x, y = ints(s.split())
    >>> color, x, y
    ('red', 1, 2)
    """
    return [maybeint(s, mixedstring) for s in strings]

def maybeint(s, mixedstring='error'):
    """ See ints(...) """
    if re.search('[0-9]', s):
        try:
            return int(s)
        except ValueError:
            if mixedstring == 'error':
                raise
            elif mixedstring == 'str':
                return s
            elif mixedstring == 'int':
                return int(re.search('-?\d+', s).group(0))
            else:
                raise ValueError('Invalid value for mixedstring: ' + mixedstring)
    else:
        return s

def findint(s):
    return maybeint(s, 'int')

def findints(s):
    """
    >>> findints('1_-2__3.45')
    [1, -2, 3, 45]
    """
    return ints(re.findall('-?\d+', s))

def consecutives(seq, n=2):
    """
    >>> [''.join(t) for t in consecutives('abcd')]
    ['ab', 'bc', 'cd']
    >>> [''.join(t) for t in consecutives('abcd', 3)]
    ['abc', 'bcd']
    >>> [''.join(t) for t in consecutives('abcd', 5)]  # seq is too short
    []
    """
    prevs = []
    for item in seq:
        prevs.append(item)
        if len(prevs) == n:
            yield tuple(prevs)
            prevs.pop(0)

def transpose(m):
    """
    >>> transpose([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
    return [list(i) for i in zip(*m)]

def one(seq):
    """
    >>> one([2])
    2
    >>> one({2})
    2
    >>> one('2')
    '2'
    >>> one('22')
    Traceback (most recent call last):
    AssertionError: Not length 1: 22
    """
    assert len(seq) == 1, f'Not length 1: {seq}'
    for item in seq:
        return item

# enumerate
# ascii_lowercase ascii_lowercase
# defaultdict namedtuple Counter _replace
# combinations permutations product combinations_with_replacement
# lru_cache maxsize
