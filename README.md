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
