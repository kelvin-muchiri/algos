"""
Binary Search

References:
https://www.geeksforgeeks.org/binary-search/
https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
https://stackoverflow.com/a/57703680/3247914

"""

import unittest


def binary_search_iterative(arr, start, end, num):
    """Iterative binary search

    Time complexity: O(log n)
    Space complexity: O(1)
    """
    while start <= end:
        mid = start + (end - start) // 2

        if (arr[mid] < num):
            start = mid + 1
        elif (arr[mid] == num):
            return mid
        else:
            end = mid - 1

    return -1


def binary_search_recursive(arr, start, end, num):
    """Recursive binary search

    Time complexity: O(log n)
    Space complexity: O(log n)
    """
    if start > end:
        return -1

    mid = start + (end - start) // 2

    if arr[mid] == num:
        return mid

    if num < arr[mid]:
        return binary_search_recursive(arr, start, mid - 1, num)

    return binary_search_recursive(arr, mid + 1, end, num)


class BinarySearchTestCase(unittest.TestCase):
    def test_iterative(self):
        arr_1 = [2, 3, 4, 10, 40]
        self.assertEqual(binary_search_iterative(
            arr_1, 0, len(arr_1) - 1, 10), 3)

    def test_recusrive(self):
        arr_1 = [2, 3, 4, 10, 40]
        self.assertEqual(binary_search_recursive(
            arr_1, 0, len(arr_1) - 1, 10), 3)


if __name__ == "__main__":
    unittest.main()
