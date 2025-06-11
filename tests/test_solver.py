import unittest
from river_crossing.solver import solve


class TestSolver(unittest.TestCase):
    def test_solve_small(self):
        moves = solve(2, 2)
        self.assertIsNotNone(moves)
        self.assertTrue(len(moves) > 0)


if __name__ == "__main__":
    unittest.main()
