"""Utilities for exploring solution lengths and runtime."""

from .solver import solve
from .visualize import format_moves
import time


def find_solutions(max_n: int = 3, k: int = 2):
    """Return a mapping from ``n`` to ``(moves, runtime)``."""
    results = {}
    for n in range(1, max_n + 1):
        start = time.time()
        sol = solve(n, k)
        elapsed = time.time() - start
        results[n] = (sol, elapsed)
    return results


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Find river crossing solutions")
    parser.add_argument("max_n", type=int, nargs="?", default=3, help="maximum number of pairs")
    parser.add_argument("-k", type=int, default=2, help="boat capacity")
    args = parser.parse_args()

    for n, (moves, runtime) in find_solutions(args.max_n, args.k).items():
        if moves is None:
            print(f"n={n} k={args.k}: no solution (computed in {runtime:.2f}s)")
        else:
            formatted = format_moves(moves)
            print(f"n={n} k={args.k}: {len(moves)} steps in {runtime:.2f}s -> {formatted}")


if __name__ == "__main__":
    main()
