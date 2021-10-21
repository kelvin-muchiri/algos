"""
Given a binary tree, determine if it is height-balanced

A binary tree in which the left and right subtrees of
every node differ in height by no more than 1
"""

import unittest


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(node):
    """Attempted solution"""
    if node is None:
        return True

    if node.left is None and node.right is None:
        return True

    # get the height left subtree and right subtree
    height_left = get_node_height(node.left)
    height_right = get_node_height(node.right)

    return abs(height_left - height_right) <= 1


def get_node_height(node):
    queue = []
    queue.append(node)
    height = 0

    while queue:
        r = queue.pop(0)

        if r.left or r.right:
            height += 1

            if r.left:
                queue.append(r.left)

            if r.right:
                queue.append(r.right)

    return height


def height(self, root: TreeNode) -> int:
    if not root:
        # An empty tree has height -1
        return -1

    return 1 + max(self.height(root.left), self.height(root.right))


def isBalanced(self, root: TreeNode) -> bool:
    """Solution

    A tree T rooted at r is balanced if and only if the height
    of its two children are within 1 of each other and the subtrees at
    each child are also balanced.

    Just because the root left and right subtree are balanced, doesn't
    mean it's true for every single node. So we have to check the left
    subtree and right subtree as well
    """
    # An empty tree satisfies the definition of a balanced tree
    if not root:
        return True

    # Check if subtrees have height within 1. If they do, check if the
    # subtrees are balanced
    return abs(self.height(root.left) - self.height(root.right)) < 2 \
        and self.isBalanced(root.left) \
        and self.isBalanced(root.right)


class Solution:
    # Return whether or not the tree at root is balanced while also returning
    # the tree's height
    def isBalancedHelper(self, root):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1

        # Check subtrees to see if they are balanced.
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0

        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedHelper(root)[0]


class NodeHeightTestCase(unittest.TestCase):
    def test_height(self):
        node = TreeNode(3)
        node.left = TreeNode(9)
        node.right = TreeNode(20)
        node.right.left = TreeNode(15)
        node.right.right = TreeNode(7)

        self.assertEqual(get_node_height(node), 2)


if __name__ == "__main__":
    unittest.main()
