"""Utilities for exploring solution lengths and runtime."""

from .solver import solve
from .visualize import format_moves, format_moves_paper
from .strategy import strategy_k4, verify_moves
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


def write_table(path: str, n_min: int = 2, n_max: int = 10, k_min: int = 2, k_max: int = 4):
    """Generate a CSV table of solutions for ranges of n and k."""

    import csv

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "k", "steps", "runtime_s", "moves"])
        for k in range(k_min, k_max + 1):
            for n in range(n_min, n_max + 1):
                start = time.time()
                moves = solve(n, k)
                runtime = time.time() - start
                if moves is None:
                    writer.writerow([n, k, None, f"{runtime:.2f}", "None"])
                else:
                    writer.writerow([
                        n,
                        k,
                        len(moves),
                        f"{runtime:.2f}",
                        format_moves_paper(moves),
                    ])


def write_k4_strategy_table(path: str, n_min: int = 6, n_max: int = 60):
    """Generate a CSV table using the specialized k=4 strategy."""

    import csv, time

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "steps", "moves"])
        for n in range(n_min, n_max + 1):
            start = time.time()
            moves = strategy_k4(n)
            ok = verify_moves(n, moves)
            runtime = time.time() - start
            steps = len(moves) if ok else None
            writer.writerow([n, steps, format_moves_paper(moves)])


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Find river crossing solutions")
    parser.add_argument("max_n", type=int, nargs="?", default=3, help="maximum number of pairs")
    parser.add_argument("-k", type=int, default=2, help="boat capacity")
    parser.add_argument("--table", type=str, help="write CSV table to path")
    parser.add_argument("--k4table", type=str, help="write k=4 strategy CSV")
    args = parser.parse_args()

    if args.k4table:
        write_k4_strategy_table(args.k4table, 6, args.max_n)
    elif args.table:
        write_table(args.table, 2, args.max_n, 2, args.k)
    else:
        for n, (moves, runtime) in find_solutions(args.max_n, args.k).items():
            if moves is None:
                print(f"n={n} k={args.k}: no solution (computed in {runtime:.2f}s)")
            else:
                formatted = format_moves(moves)
                print(f"n={n} k={args.k}: {len(moves)} steps in {runtime:.2f}s -> {formatted}")


if __name__ == "__main__":
    main()
