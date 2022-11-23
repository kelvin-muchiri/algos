""""
https://www.interviewbit.com/problems/palindrome-partitioning/
https://www.youtube.com/watch?v=3jvWodd7ht0&ab_channel=NeetCode
https://leetcode.com/problems/palindrome-partitioning/solution/

The aim is to partition the string into all possible palindrome combinations.
To achieve this, we must generate all possible substrings of a string by partitioning
at every index until we reach the end of the string.

Time Complexity:
O(N * 2^N) where N is the length of the string. This is the worst case time
complexity when all the possible substrings are palindrome. There could
be 2 ^ N possible substrings in the worst case. For each substring, it takes
o(N) to generate the substring and determine if its palindrome or not
Space Complexity:
O(N) where N is the length of the string. The space will be used to store the
recursion stack
"""

import unittest


class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        result = []
        partition = []
        self.partition_2(result, partition, A, 0)
        return result

    def partition_2(self, result, partition, A, i):
        """
        We use DFS, we recursively expand potential candidates until the defined
        goal is achieved. After that we backtrack to explore the next potential
        candidate
        """
        # our goal is achieved when we reach the end of the string
        if i == len(A):
            result.append(list(partition.copy()))
            return

        # generate all possible substrings beginning at index i to the end of
        # the string
        for j in range(i, len(A)):
            # for each of the substrings generated, check if it is palindrome
            if self.isPalindrome(A[i:j+1]):
                # if substring is a palindrome, add it to the current list and
                # perform a DFS on the remaing substring
                partition.append(A[i:j+1])
                # look for additional palindromes
                self.partition_2(result, partition, A, j+1)
                # back track to explore the next potential candidate if start index
                # is greater than or equal to the string length
                partition.pop()

    def isPalindrome(self, A):
        """Our constraint. String must be a palindrome"""
        return list(A) == list(reversed(A))


class PalindromPartitionTestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        self.assertEqual(sol.partition('aab'), [['a', 'a', 'b'], ['aa', 'b']])


if __name__ == "__main__":
    unittest.main()
