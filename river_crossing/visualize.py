from typing import Iterable

def format_moves(moves: Iterable[Iterable[str]]) -> str:
    return " -> ".join(["[" + ",".join(m) + "]" for m in moves])
