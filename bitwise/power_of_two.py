"""
How to check if a given number is a power of 2
"""

import unittest


def is_power_of_two(x):
    """Return true if a number is a power of 2 false otherwise

    The number is repeatedly divided by 2, if we end up with on 1,
    it's a power of 2, otherwise not

    Time complexity is O(log N)
    """

    if x == 0:
        return False

    else:
        while x % 2 == 0:
            x /= 2

        return x == 1


def is_power_of_two_bitwise(x):
    """Use bitwise operations to check if a number is a power of 2

    Properties of numbers which are powers of 2 is that they have only one bit set
    in their binary representation

    https://www.hackerearth.com/practice/notes/bit-manipulation/
    """
    return x and ~(x & (x - 1))


class PowerOfTwoTestCase(unittest.TestCase):
    def test_is_power_of_two(self):
        self.assertTrue(is_power_of_two(4))

    def test_is_power_of_two_bitwise(self):
        self.assertTrue(is_power_of_two(4))
        self.assertFalse(is_power_of_two(7))


if __name__ == "__main__":
    unittest.main()
