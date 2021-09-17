""""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""

import unittest


def _is_permutation(s1_lookup, permutation_lookup):
    is_permutation = True

    for key, value in s1_lookup.items():
        if permutation_lookup.get(key) is None or permutation_lookup.get(key) != value:
            return False

    return is_permutation


def is_permutation(str1, str2):
    is_permutation = False
    i = 0
    s1_lookup = {}

    for char in str1:
        if s1_lookup.get(char):
            s1_lookup[char] += 1

        else:
            s1_lookup[char] = 1

    while not is_permutation and i < len(str2):
        # if char is in str1, check if the next str1.length chars are
        # a permutation of string1
        j = 0
        k = i
        stop = False
        permutation_lookup = {}

        while not stop and j < len(str1) and k < len(str2):
            current_perm_char = str2[k]

            if not s1_lookup.get(current_perm_char):
                stop = True

            else:
                if permutation_lookup.get(current_perm_char):
                    permutation_lookup[current_perm_char] += 1

                else:
                    permutation_lookup[current_perm_char] = 1

            j += 1
            k += 1

        if _is_permutation(s1_lookup, permutation_lookup):
            is_permutation = True

        i += 1

    return is_permutation


class PermutationStringTestCase(unittest.TestCase):

    def test_attempt(self):
        self.assertTrue(is_permutation("ab", "eidbaooo"))
        self.assertFalse(is_permutation("ab", "eidboaoo"))
        self.assertFalse(is_permutation("hello", "ooolleoooleh"))
        self.assertTrue(is_permutation("adc", "dcda"))

    def test_solution(self):
        self.assertTrue(is_permutation_sol("ab", "eidbaooo"))
        self.assertFalse(is_permutation_sol("ab", "eidboaoo"))
        self.assertFalse(is_permutation_sol("hello", "ooolleoooleh"))
        self.assertTrue(is_permutation_sol("adc", "dcda"))


NUM_CHARS = 26


def _is_permutation_sol(s1_lookup, s2_lookup):
    is_permutation = True

    for i in range(NUM_CHARS):
        if s1_lookup[i] != s2_lookup[i]:
            return False

    return is_permutation


def is_permutation_sol(str1, str2):
    """Almost same implementation as the attempted solution, we use
    an array to store the frequencies. The attempt failed with time exceeded
    for large inputs
    """

    if len(str1) > len(str2):
        return False

    s1_lookup = [0] * NUM_CHARS  # 26 letters of the aplhabet

    for char in str1:
        s1_lookup[ord(char) - ord('a')] += 1

    is_permutation = False
    i = 0

    while not is_permutation and i <= len(str2) - len(str1):
        # if char is in str1, check if the next str1.length chars are
        # a permutation of string1
        j = 0
        permutation_lookup = [0] * NUM_CHARS

        while j < len(str1):
            permutation_lookup[ord(str2[i + j]) - ord('a')] += 1

            j += 1

        if _is_permutation_sol(s1_lookup, permutation_lookup):
            is_permutation = True

        i += 1

    return is_permutation


if __name__ == "__main__":
    unittest.main()
