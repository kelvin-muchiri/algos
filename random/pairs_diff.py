"""
Example: Given an array of distinct integer values, count the number
of pairs of integers that have difference k. For example,
given the array {1, 7, 5, 9, 2, 12, 3} and the difference k = 2,
there are four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9)
"""
import unittest


def difference_count(k, alist):
    lookup = set()
    pairs = []

    for i in range(len(alist)):
        lookup.add(alist[i])

    for i in range(len(alist)):
        one = alist[i]
        two = abs(k + alist[i])

        if two in lookup:
            pairs.append((one, two))

    print(pairs)

    return len(pairs)


class DifferenceTestCase(unittest.TestCase):
    def test_returns_correctly(self):
        self.assertEqual(difference_count(2, [1, 7, 5, 9, 2, 12, 3]), 4)
        self.assertEqual(difference_count(3, [1, 5, 3, 4, 2]), 2)


if __name__ == "__main__":
    unittest.main()
