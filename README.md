# River Crossing Codex

This project contains a simple implementation of the "River Crossing" puzzle
described in the accompanying paper. The puzzle features `N` actor–agent pairs
that must cross a river in a boat with capacity `k` while respecting a safety
constraint: an actor may not be with another agent unless their own agent is
present. The implementation includes:

- `river_crossing.environment`: state representation and move generation
- `river_crossing.solver`: a breadth‑first search solver
- `river_crossing.analysis`: helper utilities for exploring solutions
- `river_crossing.visualize`: simple formatting for move sequences

Unit tests are provided under the `tests/` directory.

## Running Tests

```bash
python -m unittest discover tests
```

## Exploring Solutions

The included BFS solver explores roughly `O(3^n)` states, so runtime grows
exponentially with the number of pairs `n`. Practical experiments show that
boat capacity `k=4` still allows solutions to be found for `n=10` within half a
minute on typical hardware.

For `k=4` and `n \ge 6` a closed-form shuttle strategy is implemented in
`river_crossing.strategy`. It produces solutions of length `2n-3` without
search. You can export a CSV of these moves for larger `n` via:

```bash
python -m river_crossing.analysis 60 --k4table solution_k4.csv
```

You can search for solutions up to a given `n` via:

```bash
python -m river_crossing.analysis 10 -k 4
```

To generate a CSV table of solutions in the format required by the paper
prompts, you can run:

```bash
python -m river_crossing.analysis 10 -k 4 --table solutions.csv
```

