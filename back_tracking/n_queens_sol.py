"""
The n-queens puzzle is the problem of placing n queens on a (n*n) chessboard such t
hat no two queens can attack each other.
Given an integer n, find all distinct solutions to the n-queens puzzle.
Each solution contains distinct board configurations of the n-queens' placement,
where the solutions are a permutation of [1,2,3..n] in increasing order, here the number in
the ith place denotes that the ith-column queen is placed in the row with that number.
For eg below figure represents a chessboard [3 1 4 2]

https://practice.geeksforgeeks.org/problems/n-queen-problem0315/1
"""

result = []


class Solution:
    def _is_safe(self, board, row, col, N):
        # check row on the left side
        for i in range(col):
            if board[row][i]:
                return False

        # check upper diagonal on the left side
        i = row - 1
        j = col - 1

        while i >= 0 and j >= 0:
            if board[i][j]:
                return False

            i -= 1
            j -= 1

        # check lower diagonal on the left side
        i = row + 1
        j = col - 1

        while i < N and j >= 0:
            if board[i][j]:
                return False

            i += 1
            j -= 1

        return True

    def _n_queen(self, board, col, N):
        # base case if all queens are placed
        # return true
        if col == N:
            v = []
            for i in board:
                for j in range(len(i)):
                    if i[j] == 1:
                        v.append(j+1)

            result.append(v)
            return True

        # consider column and try placing queens in all rows
        res = False
        for i in range(N):
            # check if its safe to place queen
            if self._is_safe(board, i, col, N):
                # place queen on board
                board[i][col] = 1

                # recur to place rest of the queens
                res = self._n_queen(board, col + 1, N)

                # if placing the queen in board[i][col]
                # doesn't lead to a solution then undo
                board[i][col] = 0

        # queen cannot be placed in any row in this col
        return res

    def nQueen(self, n):
        result.clear()
        board = [[0 for j in range(n)]
                 for i in range(n)]
        self._n_queen(board, 0, n)
        result.sort()

        return result
