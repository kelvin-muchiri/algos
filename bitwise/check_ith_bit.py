"""
Check if the ith bit is set in the binary form of the given number
"""
import unittest


def check_ith_bit(n, i):
    """
    AND n with 2^i. The binary form of 2 ^ i contains only ith bit as set, else
    every bit is 0. If the ith bit is set, when we AND it with n, it will return
    a non zero number, else 0 will be returned

    https://www.hackerearth.com/practice/notes/bit-manipulation/
    """

    # using the left shift operator 2^i = 1 << i
    return n & (1 << i)


class CheckIthBitTestCase(unittest.TestCase):
    def test_check_ith_bit(self):
        self.assertTrue(4, 3)


if __name__ == "__main__":
    unittest.main()
