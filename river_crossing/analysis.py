from .solver import solve


def find_solutions(max_n=3, k=2):
    results = {}
    for n in range(1, max_n + 1):
        sol = solve(n, k)
        results[(n, k)] = sol
    return results
