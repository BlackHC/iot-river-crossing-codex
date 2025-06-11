class RiverCrossingState:
    """Represents the state of the river crossing puzzle."""
    def __init__(self, actors_left, agents_left, boat_left=True):
        self.actors_left = frozenset(actors_left)
        self.agents_left = frozenset(agents_left)
        self.boat_left = boat_left

    def is_goal(self):
        return not self.actors_left and not self.agents_left and not self.boat_left

    def __hash__(self):
        return hash((self.actors_left, self.agents_left, self.boat_left))

    def __eq__(self, other):
        return (
            self.actors_left == other.actors_left
            and self.agents_left == other.agents_left
            and self.boat_left == other.boat_left
        )

    def __repr__(self):
        side = 'left' if self.boat_left else 'right'
        return f"State(actors_left={sorted(self.actors_left)}, agents_left={sorted(self.agents_left)}, boat_{side})"


def check_safety(actors_left, agents_left, actors_right, agents_right):
    """Check the safety constraint on both sides of the river."""
    def safe(actors, agents):
        for i in actors:
            if i not in agents and (agents - {i}):
                return False
        return True

    return safe(actors_left, agents_left) and safe(actors_right, agents_right)


def possible_moves(state, n, k):
    """Generate all valid moves from the given state."""
    actors_left = set(state.actors_left)
    agents_left = set(state.agents_left)
    actors_right = set(range(1, n + 1)) - actors_left
    agents_right = set(range(1, n + 1)) - agents_left

    current_side = 'left' if state.boat_left else 'right'
    if state.boat_left:
        actors_src, agents_src = actors_left, agents_left
    else:
        actors_src, agents_src = actors_right, agents_right

    individuals_src = {f"a{i}" for i in actors_src} | {f"A{i}" for i in agents_src}
    individuals_list = sorted(individuals_src)

    from itertools import combinations

    for r in range(1, min(k, len(individuals_list)) + 1):
        for combo in combinations(individuals_list, r):
            next_actors_left = actors_left.copy()
            next_agents_left = agents_left.copy()
            moving_actors = {int(x[1:]) for x in combo if x.startswith('a')}
            moving_agents = {int(x[1:]) for x in combo if x.startswith('A')}
            if state.boat_left:
                next_actors_left -= moving_actors
                next_agents_left -= moving_agents
            else:
                next_actors_left |= moving_actors
                next_agents_left |= moving_agents
            next_state = RiverCrossingState(next_actors_left, next_agents_left, not state.boat_left)
            next_actors_right = set(range(1, n + 1)) - next_state.actors_left
            next_agents_right = set(range(1, n + 1)) - next_state.agents_left
            if check_safety(next_state.actors_left, next_state.agents_left, next_actors_right, next_agents_right):
                yield combo, next_state
