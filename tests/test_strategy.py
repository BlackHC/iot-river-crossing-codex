import unittest
from river_crossing.strategy import strategy_k4, verify_moves

class TestStrategyK4(unittest.TestCase):
    def test_full_range(self):
        for n in range(6, 61):
            moves = strategy_k4(n)
            self.assertTrue(verify_moves(n, moves))
            # Expect length close to 2n-3
            self.assertLessEqual(abs(len(moves) - (2*n - 3)), 1)

if __name__ == "__main__":
    unittest.main()
