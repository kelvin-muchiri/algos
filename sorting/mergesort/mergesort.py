"""
Divide and conquer

Divide an arary into two halves, call itself for the two halves
then merge the two sorted halves.

Key process is merge(arr, l, m, r). Assumes arr[l to m] and arr[m+1 to r]
are sorted and merges the two sub arrays into one

Time complexity is O(n log n)
"""
import unittest


def mergesort(arr):
    if len(arr) > 1:
        midpoint = len(arr) // 2
        left = arr[:midpoint]
        right = arr[midpoint:]

        # Call mergesort left half
        mergesort(left)
        # Call mergesort right half
        mergesort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1

            else:
                arr[k] = right[j]
                j += 1

            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


class MergeSortTestCase(unittest.TestCase):
    def test_unsorted_array(self):
        arr = [10, 7, 8, 9, 1, 5]
        mergesort(arr)
        self.assertEqual(arr,  [1, 5, 7, 8, 9, 10])

    def test_sorted_array(self):
        arr = [1, 5, 7, 8, 9, 10]
        mergesort(arr)
        self.assertEqual(arr,  [1, 5, 7, 8, 9, 10])


if __name__ == "__main__":
    unittest.main()
