""" Most obvious is 2D, but works for arbitrary dimensions """

def _make_grid_class(names, rotdir):
    class clazz:
        lst = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        tovec = { names[i]: vec for (i, vec) in enumerate(lst) }
        toname = { vec: names[i] for (i, vec) in enumerate(lst) }

        @staticmethod
        def rot(direction, rotation):
            if rotation == 'R':
                return self.lst[(self.lst.index(d) + rotdir) % 4]
            elif rotation == 'L':
                return self.lst[(self.lst.index(d) - rotdir) % 4]
            else:
                raise Exception("invalid rotation direction: " + rotation)

        @staticmethod
        def addvec(a, b):
            return tuple(x+y for x,y in zip(a,b))

        @staticmethod
        def index(mygrid, vec):
            for x in vec:
                mygrid = mygrid[x]
            return mygrid

        @staticmethod
        def absmanhattan(vec):
            return sum(abs(x) for x in vec)
    return clazz

gridcardinal = _make_grid_class('ENWS', -1)
gridnatural = _make_grid_class('RULD', -1)
griddigital = _make_grid_class('RULD', 1)
