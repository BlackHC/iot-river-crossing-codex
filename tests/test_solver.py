import unittest
from river_crossing.solver import solve
from river_crossing.visualize import format_moves_paper


class TestSolver(unittest.TestCase):
    def test_solve_small(self):
        moves = solve(2, 2)
        self.assertIsNotNone(moves)
        self.assertTrue(len(moves) > 0)

    def test_format_paper(self):
        moves = [['A1', 'a1']]
        formatted = format_moves_paper(moves)
        self.assertEqual(formatted, 'moves = [["A_1", "a_1"]]')


if __name__ == "__main__":
    unittest.main()

