import unittest

def mergesort(arr):
    """Sort an array of items using mergesort."""
    if len(arr) > 1:
        midpoint = len(arr) // 2
        left = arr[:midpoint]
        right = arr[midpoint:]

        # Call merge sort on left half
        mergesort(left)
        # Call merge sort on right half
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
        
        # Check if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def binary_search(arr, item):
    """Search for an item in the list using binary search."""
    if len(arr) == 0:
        return False
    
    midpoint = len(arr) // 2

    if arr[midpoint] == item:
        return True
    
    else:
        if item < arr[midpoint]:
            return binary_search(arr[:midpoint], item)
        
        else:
            return binary_search(arr[midpoint + 1:], item)


def get_largest_denomination(coinList, amount):
    """Get the largest denomination that can make the amount."""
    largest_denomination = coinList[-1]
    i = len(coinList) - 2

    while i >= 0 and coinList[i] > amount:
        largest_denomination = coinList[i]
        i -= 1
    
    return largest_denomination


def _coin_change(coinList, amount, coin_change = []):
    if len(coinList) == 0:
        # We have not found denominations that we can give
        # change
        return -1

    # Get the largest denomination
    largest_denomination = get_largest_denomination(coinList, amount)
    # Get the max number of coins for the required for the largest denomination
    largest_denomination_coins_no = amount // largest_denomination
    coin_change = coin_change + [largest_denomination] * largest_denomination_coins_no
    remainder_amount = amount - (largest_denomination * largest_denomination_coins_no)

    if remainder_amount == 0:
        # Change was satisfied, return
        return len(coin_change)

    # Get the remaining amount and check if we have a matching denomination
    # for the remaining amount
    # Get the remaining list of denominations
    remaining_coin_list = coinList[:-1]

    if binary_search(remaining_coin_list, remainder_amount):
        # We have a matching denomination for our remaining amount
        coin_change.append(remainder_amount)
        return len(coin_change)
    
    return _coin_change(remaining_coin_list, remainder_amount, coin_change) 
    


def coin_change(coinList, amount):
    """Return the fewest number of coins needed to make given amount."""
    if amount == 0:
        # No change required
        return 0

    # Sort the coin denominations in ascending order
    mergesort(coinList)

    # If there is a denomination matching our amount, 
    # return 1
    if binary_search(coinList, amount):
        return 1
    
    return _coin_change(coinList, amount)
    


class MergeSortTestCase(unittest.TestCase):
    def test_unsorted_array(self):
        arr = [10, 7, 8, 9, 1, 5]
        mergesort(arr)
        self.assertEqual(arr,  [1, 5, 7, 8, 9, 10])

    def test_sorted_array(self):
        arr = [1, 5, 7, 8, 9, 10]
        mergesort(arr)
        self.assertEqual(arr,  [1, 5, 7, 8, 9, 10])
    
    def test_negative_numbers(self):
        arr = [1, -5, -7, 8, 9, -10]
        mergesort(arr)
        self.assertEqual(arr,  [-10, -7, -5, 1, 8, 9])


class BinarySearchTestCase(unittest.TestCase):
    def test_existing(self):
        arr = [1, 5, 7, 8, 9, 10]
        self.assertEqual(binary_search(arr, 7), True)
    
    def test_non_existent(self):
        arr = [1, 5, 7, 8, 9, 10]
        self.assertEqual(binary_search(arr, 23), False)

class CoinChangeTestCase(unittest.TestCase):
    def test_one_coin_change(self):
        self.assertEqual(coin_change([1, 2, 5], 5), 1)
    
    def test_correct_change(self):
        self.assertEqual(coin_change([1, 2, 5], 11), 3)
    
    def test_no_change_available(self):
        self.assertEqual(coin_change([2], 3), -1)
    
    def test_zero_amount(self):
         self.assertEqual(coin_change([1, 2, 5], 0), 0)

    def test_one(self):
        self.assertEqual(coin_change([1], 2), 2)
    def test_greedy(self):
        self.assertEqual(coin_change([186,419,83,408], 6249), 20)

if __name__ == '__main__':
    unittest.main()

