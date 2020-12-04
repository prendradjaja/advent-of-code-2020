import unittest
from grid import griddigital as digital, gridnatural as natural, gridcardinal as cardinal, make_grid_class

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

source = make_grid_class('RDLU', 1)
g = [
  'o.........',
  '.b.c......',
  '..........',
  '..a.......',
  '..........',
]

class TestSource(unittest.TestCase):

    def test_movement(self):
        # Can move with direction names
        pos = (0, 0)
        pos = source.move(pos, 'D', 3)
        pos = source.move(pos, 'R', 2)
        self.assertEqual('a', source.index(g, pos), 'Position is ' + str(pos))
        pos = source.move(pos, 'U', 2)
        pos = source.move1(pos, 'L')
        self.assertEqual('b', source.index(g, pos), 'Position is ' + str(pos))

        # Can move with a unit vector
        pos = source.move(pos, (0, 1), 2)
        self.assertEqual('c', source.index(g, pos), 'Position is ' + str(pos))

    def test_rotation(self):
        pos = (0, 0)

        # Can rotate L
        curdir = source.tovec['L']
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

if __name__ == '__main__':
    unittest.main()
