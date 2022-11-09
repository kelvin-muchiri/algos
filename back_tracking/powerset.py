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
"""


class Solution:

    def subsets(self, nums):
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # decision not to include nums[i]
            subset.pop()  # pop the element we've just added
            dfs(i + 1)

        dfs(0)

        return res


if __name__ == "__main__":
    N = 4
    board = [[0 for j in range(N)] for i in range(N)]

    for i in range(N):
        print(board[i])
