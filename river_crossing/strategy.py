"""Specialized strategies for the river crossing puzzle."""
from typing import Iterable, List, Tuple
from .environment import RiverCrossingState, check_safety

Move = Tuple[str, ...]


def strategy_k4(n: int) -> List[Move]:
    """Return a non-search strategy for boat capacity k=4.

    The sequence follows a shuttle pattern using pair 1 to ferry
    groups of four. It yields ``2n-3`` moves for ``n>=6`` and has
    been validated against the BFS solver for small ``n``.
    """
    if n < 5:
        raise ValueError("strategy_k4 requires n>=5")

    moves: List[Move] = []
    # Initial shuttle setup transferring pairs 1..5
    moves.append(("A1", "a1"))
    moves.append(("A1",))
    moves.append(tuple(f"a{i}" for i in range(2, min(n + 1, 6))))
    moves.append(("a1",))
    moves.append(tuple(f"A{i}" for i in range(2, min(n + 1, 6))))
    moves.append(("A2", "a2"))
    moves.append(("A1", "A2", "a1", "a2"))

    # Remaining pairs are ferried one by one with pair1 acting as shuttle
    for i in range(6, n + 1):
        moves.append(("A1", "a1"))
        moves.append(("A1", f"A{i}", "a1", f"a{i}"))

    return moves


def verify_moves(n: int, moves: Iterable[Move]) -> bool:
    """Check that ``moves`` solve the puzzle for ``n``."""
    state = RiverCrossingState(set(range(1, n + 1)), set(range(1, n + 1)), True)
    for mv in moves:
        moving_actors = {int(x[1:]) for x in mv if x.startswith("a")}
        moving_agents = {int(x[1:]) for x in mv if x.startswith("A")}
        if state.boat_left:
            actors_left = set(state.actors_left) - moving_actors
            agents_left = set(state.agents_left) - moving_agents
        else:
            actors_left = set(state.actors_left) | moving_actors
            agents_left = set(state.agents_left) | moving_agents
        next_state = RiverCrossingState(actors_left, agents_left, not state.boat_left)
        actors_right = set(range(1, n + 1)) - next_state.actors_left
        agents_right = set(range(1, n + 1)) - next_state.agents_left
        if not check_safety(
            next_state.actors_left, next_state.agents_left, actors_right, agents_right
        ):
            return False
        state = next_state
    return state.is_goal()
