"""
https://www.pramp.com/challenge/N5LYMbYzyOtbpovQoYPX
https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/
"""
import unittest


def binary_search(arr, start, end, num):
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] < num:
            start = mid + 1
        elif arr[mid] == num:
            return mid
        else:
            end = mid - 1

    return -1


class Solution1:
    def find_pivot(self, arr):
        """Find the pivot using binary search"""

        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if mid == 0 or arr[mid] < arr[mid-1]:
                return mid

            if arr[mid] > arr[0]:
                start = mid + 1
            else:
                end = mid - 1

        return 0

    def shifted_arr_search(self, shiftArr, num):
        pivot = self.find_pivot(shiftArr)

        # if the element greater than the 0th element, the search is in
        # the left array, else search is in the right array

        if pivot == 0 or num < shiftArr[0]:
            return binary_search(shiftArr, pivot, len(shiftArr) - 1, num)

        return binary_search(shiftArr, 0, pivot - 1, num)


class Solution2:
    def search(self, arr, l, h, key):
        if l > h:
            return -1

        mid = (l + h) // 2
        if arr[mid] == key:
            return mid

        # If arr[l...mid] is sorted
        if arr[l] <= arr[mid]:

            # As this subarray is sorted, we can quickly
            # check if key lies in half or other half
            if key >= arr[l] and key <= arr[mid]:
                return self.search(arr, l, mid-1, key)
            return self.search(arr, mid + 1, h, key)

        # If arr[l..mid] is not sorted, then arr[mid... r]
        # must be sorted
        if key >= arr[mid] and key <= arr[h]:
            return self.search(arr, mid + 1, h, key)
        return self.search(arr, l, mid-1, key)

    def shifted_arr_search(self, shiftArr, num):
        return self.search(shiftArr, 0, len(shiftArr) - 1, num)


class ShiftedArraySearchTestCase(unittest.TestCase):
    def test_solution1(self):
        solution1 = Solution1()
        self.assertEqual(solution1.shifted_arr_search([2], 2), 0)
        self.assertEqual(solution1.shifted_arr_search(
            [9, 12, 17, 2, 4, 5], 2), 3)

    def test_solution2(self):
        solution2 = Solution2()
        self.assertEqual(solution2.shifted_arr_search([2], 2), 0)
        self.assertEqual(solution2.shifted_arr_search(
            [9, 12, 17, 2, 4, 5], 2), 3)


if __name__ == "__main__":
    unittest.main()
