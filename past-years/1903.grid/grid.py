""" Many of these methods work for n dimensions """
def make_grid_class(names, rotdir):
    """
    names: e.g. RDLU corresponding to `dirs` below
    rotdir: Going forward in `names` (e.g. RDLU -- R to D) is a...
      - right turn: 1
      - left turn: -1
    """

    class clazz:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        tovec = { names[i]: vec for (i, vec) in enumerate(dirs) }
        toname = { vec: names[i] for (i, vec) in enumerate(dirs) }
        neighborvecs = neivecs = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1) ]

        @staticmethod
        def move(pos, direction, n):
            unitvec = clazz.tovec[direction] if isinstance(direction, str) else direction
            vec = clazz.mulvec(unitvec, n)
            return clazz.addvec(pos, vec)

        @staticmethod
        def move1(pos, direction):
            return clazz.move(pos, direction, 1)

        @staticmethod
        def addvec(a, b):
            return tuple(x+y for x,y in zip(a,b))

        @staticmethod # TODO At what point should I just use numpy?
        def mulvec(vec, s):
            return tuple(x*s for x in vec)

        @staticmethod
        def index(mygrid, vec):
            for x in vec:
                mygrid = mygrid[x]
            return mygrid

        @staticmethod
        def absmanhattan(vec):
            return sum(abs(x) for x in vec)

        @staticmethod
        def rot(direction, rotation):
            assert rotation in ['L', 'R']
            return clazz.dirs[(clazz.dirs.index(direction) + (rotdir if rotation == 'R' else -rotdir)) % 4]

    return clazz

gridsource   = make_grid_class('RDLU', 1)  # (y, x)! For working with array in source code
gridcardinal = make_grid_class('ESWN', 1)  # (y, x)! For working with array in source code, but using cardinal directions instead of RDLU
gridplane    = make_grid_class('URDL', 1)  # (x, y)  For working with the usual Cartesian plane
