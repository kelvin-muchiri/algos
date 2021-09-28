"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to
reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""


def robot_grid(r, c):
    """
    Dynamic programming

    Complexity Analysis

    Time complexity: O(N x M).

    Space complexity: O(N x M)
    """
    grid = [[1] * c] * r

    for i in range(1, r):
        for j in range(1, c):
            grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

    return grid[r - 1][c - 1]


if __name__ == "__main__":
    print(robot_grid(3, 7))
