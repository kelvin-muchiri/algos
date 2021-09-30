"""
Divide and conquer

Pick element as pivot and partition the array around the picked pivot.

Ways of picking the pivot:

1. Always pick the first element
2. Always pick the last element
3. Pick random
4. Pick median

The key process is the partition process. Pick x of array as pivot,
put x at its correct position in sorted array, put elements smaller
than x before x, elements greater than x after x. Do this in linear
time.

Analysis:

T(n) = T(k) + T(n-k-1) + O(n)

https://www.youtube.com/watch?v=7h1s2SojIRw
https://stackabuse.com/quicksort-in-python/
"""
import unittest


def partition(arr, low, high):
    """
    Pick last element of array as pivot, place element at its correct
    position, place all smaller elements to the left, larger elements
    to the right.
    """
    pivot = arr[low]
    i = low + 1
    j = high

    while i <= j:
        while i <= j and arr[i] < pivot:
            i += 1

        while i <= j and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    # return the position where the paritioning is done
    return j


def quicksort(arr, low, high):
    if low < high:
        # partitioning index is now at right place.
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)  # Before pi
        quicksort(arr, pi + 1, high)  # After pi


class QuickSortTestCase(unittest.TestCase):
    def test_unsorted_array(self):
        arr = [10, 7, 8, 9, 1, 5]
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr,  [1, 5, 7, 8, 9, 10])

    def test_sorted_array(self):
        arr = [1, 5, 7, 8, 9, 10]
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr,  [1, 5, 7, 8, 9, 10])

    def test_negative_numbers(self):
        arr = [-1, 2, -8, -10]
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [-10, -8, -1, 2])


if __name__ == "__main__":
    unittest.main()
