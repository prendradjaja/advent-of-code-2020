def addvec(a, b):
    """
    Most obvious use case is 2d, but works for n-dimensional case too

    >>> addvec((1, 2), (10, 20))
    (11, 22)
    >>> addvec((1, 2, 3), (10, 20, 30))
    (11, 22, 33)
    """
    return tuple(x+y for x,y in zip(a,b))

def index(grid, vec):
    """
    Most obvious use case (hence name 'grid') is 2d, but works for n-dimensional case too

    >>> g = [['a', 'b'], ['c', 'd']]
    >>> index(g, [1, 0])
    'c'
    """
    for x in vec:
        grid = grid[x]
    return grid

def absmanhattan(vec):
    return sum(abs(x) for x in vec)


# TODO how do i DRY this out?

class gridcardinal:
    lst = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    tovec = {
        'E': (0, 1),
        'N': (1, 0),
        'W': (0, -1),
        'S': (-1, 0),
    }
    toname = {
        (0, 1):  'E',
        (1, 0):  'N',
        (0, -1): 'W',
        (-1, 0): 'S',
    }
    @staticmethod
    def rot(direction, rotation):
        if rotation == 'R':
            return self.lst[(self.lst.index(d) - 1) % 4]
        elif rotation == 'L':
            return self.lst[(self.lst.index(d) + 1) % 4]
        else:
            raise Exception("invalid rotation direction: " + rotation)
    addvec = addvec
    index = index
    absmanhattan = absmanhattan

class gridnatural:
    lst = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    tovec = {
        'R': (0, 1),
        'U': (1, 0),
        'L': (0, -1),
        'D': (-1, 0),
    }
    toname = {
        (0, 1):  'R',
        (1, 0):  'U',
        (0, -1): 'L',
        (-1, 0): 'D',
    }
    @staticmethod
    def rot(direction, rotation):
        if rotation == 'R':
            return self.lst[(self.lst.index(d) - 1) % 4]
        elif rotation == 'L':
            return self.lst[(self.lst.index(d) + 1) % 4]
        else:
            raise Exception("invalid rotation direction: " + rotation)
    addvec = addvec
    index = index
    absmanhattan = absmanhattan

class griddigital:
    lst = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    tovec = {
        'R': (0, 1),
        'D': (1, 0),
        'L': (0, -1),
        'U': (-1, 0),
    }
    toname = {
        (0, 1):  'R',
        (1, 0):  'D',
        (0, -1): 'L',
        (-1, 0): 'U',
    }
    @staticmethod
    def rot(direction, rotation):
        if rotation == 'R':
            return self.lst[(self.lst.index(d) + 1) % 4]
        elif rotation == 'L':
            return self.lst[(self.lst.index(d) - 1) % 4]
        else:
            raise Exception("invalid rotation direction: " + rotation)
    addvec = addvec
    index = index
    absmanhattan = absmanhattan
