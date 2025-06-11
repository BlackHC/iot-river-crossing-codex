import unittest
from river_crossing.environment import RiverCrossingState, possible_moves, check_safety


class TestEnvironment(unittest.TestCase):
    def test_safety(self):
        self.assertTrue(check_safety({1}, {1}, {2}, {2}))
        # Actor 1 is with Agent 2 without Agent 1 -> unsafe
        self.assertFalse(check_safety({1}, {2}, set(), set()))

    def test_possible_moves(self):
        state = RiverCrossingState({1, 2}, {1, 2}, True)
        moves = list(possible_moves(state, 2, 2))
        self.assertTrue(moves)


if __name__ == "__main__":
    unittest.main()
