"""
Implement a function to check if a binary tree is a binary search tree.
"""
import math


def is_valid_bst(node):
    """Attempt"""
    if node is None:
        return True

    if node.left:
        # check left child
        if not node.left.val < node.val:
            return False

    if node.right:
        # check right child
        if not node.right.val > node.val:
            return False

    # check subtrees
    return is_valid_bst(node.left) and is_valid_bst(node.right)


def _is_valid_bst_sol_1(node, low, high):
    # Empty trees are valid BSTs.
    if not node:
        return True
    # The current node's value must be between low and high.
    if node.val <= low or node.val >= high:
        return False

    # The left and right subtree must also be valid.
    return (_is_valid_bst_sol_1(node.right, node.val, high) and
            _is_valid_bst_sol_1(node.left, low, node.val))


def is_valid_bst_sol_1(node):
    """Approach 1: Top down DFS

    Defining the lower limit and upper limit on the values as we move
    to the left

    Time complexity: O(N)
    Space complexity: O(N) - Space required by the recursion stack
    """
    return _is_valid_bst_sol_1(node, -math.inf, math.inf)


def inorder(root, prev):
    if not root:
        return True
    if not inorder(root.left):
        return False
    if root.val <= prev:
        return False
    prev = root.val
    return inorder(root.right, prev)


def is_valid_bst_sol_2(node):
    """Approach 2: Inorder traversal

    Previous value must be less than root val
    """
    prev = -math.inf
    return inorder(node, prev)
