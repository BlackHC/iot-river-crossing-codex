from collections import deque
from .environment import RiverCrossingState, possible_moves


def solve(n: int, k: int, max_depth: int = 1000):
    """Find a sequence of moves to solve the puzzle using BFS."""
    start = RiverCrossingState(set(range(1, n + 1)), set(range(1, n + 1)), True)
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()
        if state.is_goal():
            return path
        if len(path) >= max_depth:
            continue
        for move, next_state in possible_moves(state, n, k):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [move]))
    return None
