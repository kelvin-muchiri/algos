"""
Given a set of non-negative integers, and a value sum, determine if there is
as subset of the given sum equal to the given sum

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
"""

import unittest


def subset_sum_bruteforce(integer_set, given_sum):
    """Bruteforce solution with runtime of O(N^2)"""
    integer_list = list(integer_set)
    found = False
    i = 0

    while i < len(integer_list) and not found:
        j = i + 1

        while j < len(integer_list) and not found:
            if integer_list[j] + integer_list[i] == given_sum:
                found = True

            j += 1

        i += 1

    return found


class SubsetSumTestCase(unittest.TestCase):
    def subset_sum_bruteforce(self):
        self.assertTrue(subset_sum_bruteforce({3, 34, 4, 12, 5, 2}, 9))
        self.assertFalse(subset_sum_bruteforce({3, 34, 4, 12, 5, 2}, 30))


if __name__ == "__main__":
    unittest.main()
