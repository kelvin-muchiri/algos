"""
Problem:
Given an integer array nums, return all possible subsets (power set)

The solution must not contain duplicate subsets

Solution Summary:
For each index, we decide whether to include or exclude
Note: The left recursion is always executed first

References:
https://www.youtube.com/watch?v=REOH22Xwdkk
https://www.youtube.com/watch?v=rYkfBRtMJr8
https://www.youtube.com/watch?v=NA2Oj9xqaZQ&ab_channel=Coderbyte
"""


class Solution:

    def subsets(self, nums):
        """Time complexity O(n x 2^n)"""
        res = []
        subset = []

        def dfs(index):
            if index == len(nums):
                res.append(subset.copy())
                return

            # decision to include current element nums[i]
            subset.append(nums[index])
            dfs(index + 1)

            # decision not to include current element nums[i]
            subset.pop()  # pop the element we've just added
            dfs(index + 1)

        dfs(0)

        return res
