from collections import deque
from typing import Dict, Optional, List

from .environment import State, successors


def bfs(n: int, k: int) -> Optional[List[State]]:
    start = State(missionaries_left=n, cannibals_left=n, boat_left=True)
    if not successors(start, k, n):
        return None
    queue = deque([start])
    parents: Dict[State, Optional[State]] = {start: None}

    while queue:
        state = queue.popleft()
        if state.is_goal():
            path = []
            while state is not None:
                path.append(state)
                state = parents[state]
            return list(reversed(path))
        for next_state in successors(state, k, n):
            if next_state not in parents:
                parents[next_state] = state
                queue.append(next_state)
    return None


def has_solution(n: int, k: int) -> bool:
    return bfs(n, k) is not None

