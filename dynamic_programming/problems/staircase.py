"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3
steps at a time. Implement a method to count how many possible ways the child can
run up the stairs.

N = 4
Output = 7
1 step + 1 step + 1 step + 1 step
1 step + 2 step + 1 step
2 step + 1 step + 1 step
1 step + 1 step + 2 step
2 step + 2 step
3 step + 1 step
1 step + 3 step

Notes:
https://www.geeksforgeeks.org/count-ways-reach-nth-stair/
"""

import unittest


def find_step_recursive(n):
    """
    There are n stairs, and a person is allowed to jump next stair, skip one
    stair or skip two stairs. So there are n stairs. So if a person is standing at
    i-th stair, the person can move to i+1, i+2, i+3-th stair. A recursive function can be
    formed where at current index i the function is recursively called for i+1, i+2 and i+3 th stair.
    There is another way of forming the recursive function. To reach a stair i, a person has to jump
    either from i-1, i-2 or i-3 th stair or i is the starting stair.

    Time complexity 0(3^n)
    """
    if (n == 1 or n == 0):
        return 1
    elif (n == 2):
        return 2

    else:
        return find_step_recursive(n - 3) + find_step_recursive(n - 2) + find_step_recursive(n - 1)


lookup = []


def find_step_recursive_dynamic_bottom_up(n):
    """Solve the problem in a bottom up dynamic approach

    Time complexity: O(n)
    Space complexity: O(n)
    """
    lookup[0] = 1
    lookup[1] = 1
    lookup[2] = 2

    for i in range(3, n):
        lookup[i] = lookup[i - 3] + lookup[i - 2] + lookup[i - 1]

    return lookup[n]


topDownLookup = []


def find_step_recursive_dynamic_top_down(n):
    """Solve the problem in a top down dynamic approach"""
    if (n == 1 or n == 0):
        return 1
    elif (n == 2):
        return 2

    else:
        if n not in topDownLookup:
            topDownLookup[n] = find_step_recursive_dynamic_top_down(
                n - 3) + find_step_recursive_dynamic_top_down(n - 2) + find_step_recursive_dynamic_top_down(n - 1)

    return topDownLookup[n]


class FindStepTestCase(unittest.TestCase):
    def test_find_step_recursive(self):
        self.assertEqual(find_step_recursive(4), 7)

    def test_find_step_recursive_dynamic_bottom_up(self):
        self.assertEqual(find_step_recursive(4), 7)

    def test_find_step_recursive_dynamic_top_down(self):
        self.assertEqual(find_step_recursive(4), 7)


if __name__ == "__main__":
    unittest.main()
