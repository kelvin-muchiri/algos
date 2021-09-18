"""Given a sorted (increasing order) array with unique integer
elements, write an algo- rithm to create a binary search tree with minimal height."""

import unittest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_left(self, key):
        if self.left is None:
            self.left = TreeNode(key)

        else:
            temp = self.left
            new_node = TreeNode(key)
            self.left = new_node
            new_node.left = temp

    def insert_right(self, key):
        if self.right is None:
            self.right = TreeNode(key)

        else:
            temp = self.right
            temp.right = TreeNode(key)
            self.right = temp

    def get_root_value(self):
        return self.val

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left


def _created_bst(alist, low, high):
    if low > high:
        return None

    mid = (high + low) // 2

    if (low + high) % 2:
        mid += 1

    root = TreeNode(alist[mid])
    root.left = _created_bst(alist, low, mid - 1)
    root.right = _created_bst(alist, mid + 1, high)
    return root


def create_bst(alist):
    """Create a binary search tree given a sorted array"""

    return _created_bst(alist, 0, len(alist) - 1)


def in_order(node, result):
    """Visit BST using in order"""

    if node:
        in_order(node.get_left(), result)
        result.append(node.get_root_value())
        in_order(node.get_right(), result)


def visit_bst(node):
    result = []

    in_order(node, result)

    return result


class CreateBSTTestCase(unittest.TestCase):
    def test_prints_correctly(self):
        array1 = [1, 2, 3, 4, 5, 6, 7]
        array2 = [2, 4, 6, 8, 10, 20]
        array3 = [-10, -3, 0, 5, 9]
        array4 = [3]
        array5 = [1, 3]
        array6 = [3, 5, 8]
        array7 = [0, 1, 2, 3, 4, 5, 6]
        self.assertEqual(visit_bst(create_bst(array1)), array1)
        self.assertEqual(visit_bst(create_bst(array2)), array2)
        self.assertEqual(visit_bst(create_bst(array3)), array3)
        self.assertEqual(visit_bst(create_bst(array4)), array4)
        self.assertEqual(visit_bst(create_bst(array5)), array5)
        self.assertEqual(visit_bst(create_bst(array6)), array6)
        self.assertEqual(visit_bst(create_bst(array7)), array7)

    def test_root_is_correct(self):
        array1 = [1, 2, 3, 4, 5, 6, 7]
        array2 = [2, 4, 6, 8, 10, 20]
        bst1 = create_bst(array1)
        bst2 = create_bst(array2)
        self.assertEqual(bst1.get_root_value(), 4)
        self.assertEqual(bst2.get_root_value(), 8)


if __name__ == "__main__":
    unittest.main()
