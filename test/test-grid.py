import unittest
from grid import griddigital as digital, gridnatural as natural, gridcardinal as cardinal

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

# class TestDigital(unittest.TestCase):
#     def test_movement(self):
#         self.assertEqual(digital.tovec['L'], (-1, 0))
#         self.assertEqual(digital.tovec['L'], (-1, 0))

if __name__ == '__main__':
    unittest.main()
