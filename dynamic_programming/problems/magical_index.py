"""
A magic index in an array A[e... n-1] is defined to be an index such that
A[i] = i. Given a sorted array of distinct integers, write a method to find
a magic index, if one exists, in array A.
"""

import unittest


def magic_index(arr, low, high):

    if high >= low:
        mid = low + (high - low)//2

        if arr[mid] == mid:
            return mid

        if mid < arr[mid]:
            return magic_index(arr, low, mid-1)

        else:
            return magic_index(arr, mid + 1, high)

    else:
        return -1


class MagicIndexTestCase(unittest.TestCase):
    def test_magic_index(self):
        arr = [-10, -5, 0, 3, 7]

        return self.assertEqual(magic_index(arr, 0, len(arr) - 1), 3)


if __name__ == "__main__":
    unittest.main()
