"""
Characteristics of Dynamic Programming probles
    1. Optimal substructure - For a problem, we get to the solution by finding the optimal
    solution to each subproblem
    2. Overlapping subproblems - Problem can be broken down into smaller parts which
    need to be solved again and again

Optimal solution to each subproblem is stored so that it is not re-computed again

Approaches to dynamic programming:
    1. Memoization or Top-down DP (recursion is used)
    2. Tabulation or Bottom-up DP (iterative approach is used)

References:
https://www.scaler.com/topics/data-structures/dynamic-programming/?utm_medium=direct&utm_source=none/
"""


def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)


memo = {}


def fib_dynamic(n):
    """Solve fib in a top down approach. Uses memoization"""
    if n not in memo:
        if n == 0:
            memo[n] = 0
        elif n == 1:
            memo[n] = 1

        else:
            memo[n] = fib_dynamic(n - 1) + fib_dynamic(n - 2)

    return memo[n]


def fib_dynamic_bottom_up(n):
    """Solve fib in a bottom up approach. Uses tabulation"""
    dp = [0 for i in range(n + 1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
