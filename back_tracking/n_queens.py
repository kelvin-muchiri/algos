"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
"""

"""
Notes:

- We continue the process until all queens are placed
- If no safe place is left, we change the position of the previously placed queen
- Any cell (k,l) will be diagonal to cell (i,j) if k + l = i + j, or k - l = i - j
"""
global N
N = 4


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens
def is_safe(board, row, col):
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


def solveNQUtil(board, col):

    # Base case: If all queens are placed return true
    if col >= N:
        return True

    # Consider column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solveNQUtil(board, col + 1) == True:
                return True

            # If placing queen in board[i][col
            # doesn't lead to a solution, then
            # queen from board[i][col]
            board[i][col] = 0  # Backtrack

    # if the queen can not be placed in any row in
    # this colum col then return false
    return False


def solveNQ():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
    if solveNQUtil(board, 0) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


if __name__ == "__main__":
    solveNQ()
