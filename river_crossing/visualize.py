from typing import Iterable, List
import json

def format_moves(moves: Iterable[Iterable[str]]) -> str:
    """Simple arrow-delimited visualization for debugging."""
    return " -> ".join("[" + ",".join(m) + "]" for m in moves)


def format_moves_paper(moves: Iterable[Iterable[str]]) -> str:
    """Return moves in the format used by the paper prompts."""

    def conv(name: str) -> str:
        return f"{name[0]}_{name[1:]}"

    conv_moves: List[List[str]] = [[conv(i) for i in m] for m in moves]
    return "moves = " + json.dumps(conv_moves)

