import re

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
                return int(re.search('[0-9]+', s).group(0))
            else:
                raise ValueError('Invalid value for mixedstring: ' + mixedstring)
    else:
        return s

def findint(s):
    return maybeint(s, 'int')

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

p = print

def pfirst(*args, **kwargs):
    if not pfirst.called:
        pfirst.called = True
        print(*args, **kwargs)
    return args[0]
pfirst.called = False
pf = pfirst
