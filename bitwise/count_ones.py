"""
Count the number of ones in the binary representation of the given number

Input : n = 6
Output : 2
Binary representation of 6 is 110 and has 2 set bits

Input : n = 13
Output : 3
Binary representation of 13 is 1101 and has 3 set bits
"""

import unittest


def count_ones(n):
    """
    Running time depends on the number of ones present in the binary
    form of the given number

    So as in x-1, the rightmost 1 and bits right to it are flipped, then by
    performing x&(x-1), and storing it in x, will reduce x to a number
    containing number of ones(in its binary form) less than the previous state of x,
    thus increasing the value of count in each iteration.

    Time complexity: O(K) where K is the number of ones present in binary form

    Worst case is O(log N)

    https://www.hackerearth.com/practice/notes/bit-manipulation/
    """
    count = 0

    while n:
        n = n & (n - 1)
        count += 1

    return count


class CounOnesTestCase(unittest.TestCase):
    def test_count_ones(self):
        self.assertEqual(count_ones(6), 2)
        self.assertEqual(count_ones(13), 3)


if __name__ == "__main__":
    unittest.main()
