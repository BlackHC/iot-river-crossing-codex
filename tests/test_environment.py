import os, sys; sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from river_crossing.environment import State, is_valid, move


def test_move_validity():
    n = 3
    k = 2
    state = State(3, 3, True)
    new_state = move(state, 1, 1, k, n)
    assert new_state is not None
    assert is_valid(new_state, n)

    invalid = move(state, 0, 0, k, n)
    assert invalid is None
