"""
Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?
"""
import unittest


def is_unique_sol_1(string):
    if len(string) == 1:
        return True

    if len(string) == 2:
        if string[0] == string[1]:
            return False

        else:
            return True

    i = 0
    j = len(string) - 1
    lookup = set()

    while i < j:
        if string[i] == string[j]:
            return False

        if string[i] not in lookup:
            lookup.add(string[i])
            i += 1
        else:
            return False

        if string[j] not in lookup:
            lookup.add(string[j])
            j -= 1

        else:
            return False

    return string[i] not in lookup


def is_unique_sol_2(string):
    return len(set(string)) == len(string)


class IsUniqueTestCase(unittest.TestCase):
    def test_sol1_works(self):
        self.assertTrue(is_unique_sol_1('a'))
        self.assertTrue(is_unique_sol_1('ab'))
        self.assertTrue(is_unique_sol_1('abc'))

    def test_sol2_works(self):
        self.assertTrue(is_unique_sol_2('a'))
        self.assertTrue(is_unique_sol_2('ab'))
        self.assertTrue(is_unique_sol_2('abc'))


if __name__ == "__main__":
    unittest.main()
