from dataclasses import dataclass
from typing import List, Tuple, Optional

@dataclass(frozen=True)
class State:
    missionaries_left: int
    cannibals_left: int
    boat_left: bool

    def is_goal(self) -> bool:
        return self.missionaries_left == 0 and self.cannibals_left == 0 and not self.boat_left

def is_valid(state: State, n: int) -> bool:
    ml = state.missionaries_left
    cl = state.cannibals_left
    mr = n - ml
    cr = n - cl

    if ml < 0 or cl < 0 or ml > n or cl > n:
        return False

    if ml > 0 and cl > ml:
        return False
    if mr > 0 and cr > mr:
        return False
    return True

def move(state: State, missionaries: int, cannibals: int, k: int, n: int) -> Optional[State]:
    if missionaries < 0 or cannibals < 0:
        return None
    if missionaries + cannibals == 0 or missionaries + cannibals > k:
        return None

    if state.boat_left:
        new_state = State(
            state.missionaries_left - missionaries,
            state.cannibals_left - cannibals,
            False,
        )
    else:
        new_state = State(
            state.missionaries_left + missionaries,
            state.cannibals_left + cannibals,
            True,
        )

    if is_valid(new_state, n):
        return new_state
    return None

def successors(state: State, k: int, n: int) -> List[State]:
    succ = []
    for m in range(0, k + 1):
        for c in range(0, k + 1):
            if m + c == 0 or m + c > k:
                continue
            ns = move(state, m, c, k, n)
            if ns is not None:
                succ.append(ns)
    return succ
