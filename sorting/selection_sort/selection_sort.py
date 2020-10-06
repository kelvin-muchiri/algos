"""
Repeativelyfind the smallest element and putting it in the beginning

In every iteration pick the smallest from the unsorted sub array
and move to sorted array

Time complexity is: O(n^2)
Auxiliary space is: O(1)
"""
import unittest

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        j = i + 1

        while j < len(arr):
            if arr[j] < arr[min_index]:
                min_index = j
            
            j += 1

        # Swap found minimum element with
        # the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]


class SelectionSortTestCase(unittest.TestCase):
    def test_unsorted_array(self):
        arr = [10, 7, 8, 9, 1, 5]
        selection_sort(arr)
        self.assertEqual(arr,  [1, 5, 7, 8, 9, 10])
    
    def test_sorted_array(self):
        arr = [1, 5, 7, 8, 9, 10]
        selection_sort(arr)
        self.assertEqual(arr,  [1, 5, 7, 8, 9, 10])


if __name__ == "__main__":
    unittest.main()

        

