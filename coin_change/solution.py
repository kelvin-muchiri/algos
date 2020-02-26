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
"""

import unittest

def coin_change(coins, amount):
    minLookUp = [0] + [float('inf')] * amount
    
    for coin in coins:
        for i in range(coin, amount+1):
            minLookUp[i] = min(minLookUp[i], 1 + minLookUp[i-coin])
    
    return minLookUp[-1] if minLookUp[-1] != float('inf') else -1
    

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
        self.assertEqual(coin_change([186,419,83,408], 6249), 20)


if __name__ == '__main__':
    unittest.main()