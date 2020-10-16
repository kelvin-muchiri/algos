import unittest

"""
Time complexity of O(n^2)
"""

INT_MIN = -32767

def bottom_up_rod_cutting(c, n):
    """Build the table in a bottom up manner and return the last entry from the table."""
    maxRevenueLookUp = [0] + [float('inf')] * n

    for i in range(1, n + 1):
        max_value = INT_MIN

        for j in range(i):
            max_value = max(max_value, c[j] + maxRevenueLookUp[i-j-1])
        
        maxRevenueLookUp[i] = max_value
    
    return maxRevenueLookUp[n]




class RodCuttingTestCase(unittest.TestCase):
    def test_max_revenue(self):
        c = [1, 5, 8, 9, 10, 17, 17, 20] 
        length = len(c) 
        self.assertEqual(bottom_up_rod_cutting(c, length), 22)



if __name__ == '__main__':
    unittest.main() 