import os, sys; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from river_crossing.solver import bfs, has_solution


def test_bfs_solution():
    assert bfs(3, 2) is not None


def test_has_solution_false():
    assert not has_solution(1, 1)
