"""
Given a string A, partition A such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of A

https://www.interviewbit.com/problems/palindrome-partitioning-ii/?utm_medium=direct&utm_source=none/

References:
https://www.youtube.com/watch?v=_H8V5hJUGd0&ab_channel=takeUforward
"""

import math


class Solution:

    def minCut(self, s):
        dp = [math.inf for i in range(len(s))]
        return self.minCutUtil(0, s, dp) - 1

    def minCutUtil(self, i, string, dp):
        if i == len(string):
            return 0

        if dp[i] != math.inf:
            return dp[i]

        for j in range(i, len(string)):
            if self.is_palindrome(string[i:j + 1]):
                # get the minimum of all possibilities
                cost = 1 + self.minCutUtil(j+1, string, dp)
                dp[i] = min(dp[i], cost)

        return dp[i]

    def is_palindrome(self, string):
        return list(string) == list(string)[::-1]
