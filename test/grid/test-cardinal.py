import unittest
from grid import gridcardinal as grid
from examples import g, gcart

class TestCardinal(unittest.TestCase):

    def test_move_by_name(self):
        pos = (0, 0)
        pos = grid.move(pos, 'S', 3)
        pos = grid.move(pos, 'E', 2)
        self.assertEqual('a', grid.index(g, pos), 'Position is ' + str(pos))
        pos = grid.move(pos, 'N', 2)
        pos = grid.move1(pos, 'W')
        self.assertEqual('b', grid.index(g, pos), 'Position is ' + str(pos))

    def test_rotation(self):
        pos = (0, 0)
        curdir = grid.tovec['W']

        # Can rotate L
        curdir = grid.rot(curdir, 'L')
        pos = grid.move(pos, curdir, 3)
        curdir = grid.rot(curdir, 'L')
        pos = grid.move(pos, curdir, 2)
        self.assertEqual('a', grid.index(g, pos), 'Position is ' + str(pos))

        # Can rotate R
        curdir = grid.rot(curdir, 'R')
        curdir = grid.rot(curdir, 'R')
        pos = grid.move1(pos, curdir)
        curdir = grid.rot(curdir, 'R')
        pos = grid.move(pos, curdir, 2)
        self.assertEqual('b', grid.index(g, pos), 'Position is ' + str(pos))

if __name__ == '__main__':
    unittest.main()
