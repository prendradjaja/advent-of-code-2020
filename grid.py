""" Most obvious is 2D, but works for arbitrary dimensions """
def make_grid_class(names, rotdir):
    class clazz:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        tovec = { names[i]: vec for (i, vec) in enumerate(dirs) }
        toname = { vec: names[i] for (i, vec) in enumerate(dirs) }
        neighborvecs = neivecs = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1) ]

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
            return self.dirs[(self.dirs.index(d) + (rotdir if rotation == 'R' else -rotdir)) % 4]

    return clazz

gridcardinal = _make_grid_class('ENWS', -1)
gridnatural = _make_grid_class('RULD', -1)
griddigital = _make_grid_class('RULD', 1)
