"""
Dynamic programming problem

The optimal solution can be constructed from optical solutions of sub problems.
Can be solve either top down or bottom up.

Top Down: The idea of the algorith is to build the solution from top to bottom.
Use backtracking to cut the partial solutions in the recursive tree
which doesn't lead to a viable solution. Happens when we try to make
a change of a coin with a value greater than amount S.

Time complexity: O (S * n) where S is the amount, n is the denomination
count

Bottom Up: Before calculating F(i) we compute all min counts for amounts
upto i e.g start by making change for one cent and systematically work your way up
to the change we require. At each step of the algorithm, we already know the minimum
no.coins needed to make change for any smaller amount.

References:
https://www.youtube.com/watch?v=jgiZlGzXMBw&ab_channel=BackToBackSWE
https://www.youtube.com/watch?v=H9bfqozjoqs&ab_channel=NeetCode
"""

import unittest
from typing import List
import math


def coin_change(coins: List[int], amount: int) -> int:
    min_coins = [math.inf for i in range(amount + 1)]
    min_coins[0] = 0

    for amount in range(1, amount + 1):
        for coin in coins:
            if amount - coin >= 0:
                min_coins[amount] = min(
                    min_coins[amount], 1 + min_coins[amount-coin])

    return min_coins[-1] if min_coins[-1] != math.inf else -1


class CoinChangeTestCase(unittest.TestCase):
    def test_one_coin_change(self):
        self.assertEqual(coin_change([1, 2, 5], 5), 1)

    def test_correct_change(self):
        self.assertEqual(coin_change([1, 2, 5], 11), 3)

    def test_no_change_available(self):
        self.assertEqual(coin_change([2], 3), -1)

    def test_zero_amount(self):
        self.assertEqual(coin_change([1, 2, 5], 0), 0)

    def test_one(self):
        self.assertEqual(coin_change([1], 2), 2)

    def test_greedy(self):
        self.assertEqual(coin_change([186, 419, 83, 408], 6249), 20)


if __name__ == '__main__':
    unittest.main()
