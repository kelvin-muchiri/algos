"""
Loop from i = 1 to n - 1

Pick arr[i] and insert it into  sorted sequence arr[0 to i - 1]
"""
import unittest


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        # Move elements of arr[0 to i - 1] that are greater than
        # key to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


class MergeSortTestCase(unittest.TestCase):
    def test_unsorted_array(self):
        arr = [10, 7, 8, 9, 1, 5]
        insertion_sort(arr)
        self.assertEqual(arr,  [1, 5, 7, 8, 9, 10])

    def test_sorted_array(self):
        arr = [1, 5, 7, 8, 9, 10]
        insertion_sort(arr)
        self.assertEqual(arr,  [1, 5, 7, 8, 9, 10])


if __name__ == "__main__":
    unittest.main()
