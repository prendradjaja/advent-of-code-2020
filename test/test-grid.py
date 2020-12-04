import unittest
from grid import griddigital as digital, gridnatural as natural, gridcardinal as cardinal, make_grid_class

source = make_grid_class('RDLU', 1)  # For working with array in source code
cardinal = make_grid_class('ESWN', 1)  # For working with array in source code
g = [
  'o.........',
  '.b........',
  '..........',
  '..a.......',
  '..........',
]


class TestCommon(unittest.TestCase):

    def test_add(self):
        self.assertEqual(
            digital.addvec((1, 2), (10, 20)),
            (11, 22))
        self.assertEqual(
            digital.addvec((1, 2, 3), (10, 20, 30)),

            (11, 22, 33))
    def test_mul(self):
        self.assertEqual(
            digital.mulvec((1, 2), 10),
            (10, 20))
        self.assertEqual(
            digital.mulvec((1, 2, 3), 10),
            (10, 20, 30))

    def test_index(self):
        g2d = [ [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9], ]
        g3d = [g2d]
        self.assertEqual(6, digital.index(g2d, [1, 2]))
        self.assertEqual(6, digital.index(g3d, [0, 1, 2]))

    def test_absmanhattan(self):
        self.assertEqual(5, digital.absmanhattan([2, 3]))
        self.assertEqual(5, digital.absmanhattan([-2, 3]))
        self.assertEqual(5, digital.absmanhattan([-1, 1, 3]))

    def test_move_by_unitcvec(self):
        pos = (0, 0)
        pos = source.move(pos, (1, 0), 3)
        pos = source.move(pos, (0, 1), 2)
        self.assertEqual('a', source.index(g, pos), 'Position is ' + str(pos))

class TestSource(unittest.TestCase):

    def test_move_by_name(self):
        pos = (0, 0)
        pos = source.move(pos, 'D', 3)
        pos = source.move(pos, 'R', 2)
        self.assertEqual('a', source.index(g, pos), 'Position is ' + str(pos))
        pos = source.move(pos, 'U', 2)
        pos = source.move1(pos, 'L')
        self.assertEqual('b', source.index(g, pos), 'Position is ' + str(pos))

    def test_rotation(self):
        pos = (0, 0)
        curdir = source.tovec['L']

        # Can rotate L
        curdir = source.rot(curdir, 'L')
        pos = source.move(pos, curdir, 3)
        curdir = source.rot(curdir, 'L')
        pos = source.move(pos, curdir, 2)
        self.assertEqual('a', source.index(g, pos), 'Position is ' + str(pos))

        # Can rotate R
        curdir = source.rot(curdir, 'R')
        curdir = source.rot(curdir, 'R')
        pos = source.move1(pos, curdir)
        curdir = source.rot(curdir, 'R')
        pos = source.move(pos, curdir, 2)
        self.assertEqual('b', source.index(g, pos), 'Position is ' + str(pos))

class TestCardinal(unittest.TestCase):

    def test_move_by_name(self):
        pos = (0, 0)
        pos = cardinal.move(pos, 'S', 3)
        pos = cardinal.move(pos, 'E', 2)
        self.assertEqual('a', cardinal.index(g, pos), 'Position is ' + str(pos))
        pos = cardinal.move(pos, 'N', 2)
        pos = cardinal.move1(pos, 'W')
        self.assertEqual('b', cardinal.index(g, pos), 'Position is ' + str(pos))

    def test_rotation(self):
        pos = (0, 0)
        curdir = cardinal.tovec['W']

        # Can rotate L
        curdir = cardinal.rot(curdir, 'L')
        pos = cardinal.move(pos, curdir, 3)
        curdir = cardinal.rot(curdir, 'L')
        pos = cardinal.move(pos, curdir, 2)
        self.assertEqual('a', cardinal.index(g, pos), 'Position is ' + str(pos))

        # Can rotate R
        curdir = cardinal.rot(curdir, 'R')
        curdir = cardinal.rot(curdir, 'R')
        pos = cardinal.move1(pos, curdir)
        curdir = cardinal.rot(curdir, 'R')
        pos = cardinal.move(pos, curdir, 2)
        self.assertEqual('b', cardinal.index(g, pos), 'Position is ' + str(pos))

if __name__ == '__main__':
    unittest.main()
