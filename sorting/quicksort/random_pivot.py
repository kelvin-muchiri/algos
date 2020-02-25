"""

"""
import unittest
import random


def _partition(arr, low, high):
    """
    Pick last element of array as pivot, place element at its correct
    position, place all smaller elements to the left, larger elements
    to the right.
    """
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    j = low  # Current element

    while j < high:
        if arr[j] < pivot:
            # Current elment is smaller than or equal to pivot
            # Swap current element with arr[i]. Otherwise
            # ignore current element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

        j += 1

    # Now have pivot in its place
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def partition(arr, low, high):
    """Generate a random pivot, swap last element with random pivot."""
    random_pivot = random.randrange(low, high)

    # Swap last element and random pivot
    arr[high], arr[random_pivot] = arr[random_pivot], arr[high]
    return _partition(arr, low, high)


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
        arr = [-1,2,-8,-10]
        quicksort(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [-10,-8,-1,2])


if __name__ == "__main__":
    unittest.main()
