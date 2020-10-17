"""
How to generate all the possible subsets of a set ?
"""

import unittest
import math


def possible_subsets(A):
    """
    We know that there are 2^N possibme subsets of any given set with N elements
    """
    N = len(A)

    for i in range(int(math.pow(2, N))):
        # consider each element in the set
        subset_str = "[ "

        for j in range(N):
            # if jth bit is set in i
            if i & (1 << j):
                subset_str += "{}".format(A[j])

        print(f"{subset_str} ]")


if __name__ == "__main__":
    possible_subsets(['a', 'b', 'c'])
