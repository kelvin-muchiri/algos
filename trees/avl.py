"""
When creating a BST, we want to create a BST with the minimal height

An AVL tree is a self balancing binary tree where the
balance factor = height of left subtree - height of right subtree {-1, 0, 1}. This
must be true for all nodes

If a node say has a balance factor of 2, then it is heavy on the left side. If the
balance factor of -2, then it is heavy of the right side

Rotations are always done within 3 nodes

https://www.youtube.com/watch?v=jDM6_TnYIqE&ab_channel=AbdulBari
https://www.geeksforgeeks.org/insertion-in-an-avl-tree/
"""

import bst
import nodes


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class AVLTree:
    """Self balancing AVL BST"""

    def insert_node(self, root, node):
        """Insert node into an AVL"""
        # normal BST insert
        bst.insert_node(root, node)
        # get the balance factor
        balance_factor = self.get_balance_factor(root)

        # Case 1 - Left Left imbalance
        if balance_factor > 1 and node.data < root.left.data:
            return self.right_rotate(root)

        # Case 2 - Right Right imbalance
        if balance_factor < -1 and node.data > root.right.data:
            return self.left_rotate(root)
        # Case 3 -  Left right imbalance (2 steps, LR then RR)
        if balance_factor > 1 and node.data > root.left.data:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # Case 4 - Right left imbalance (2 steps, RR then LR)
        if balance_factor < -1 and node.data < root.right.data:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_balance_factor(self, root):
        """Get the balance factor"""
        left_height = nodes.find_height(root.left)
        right_height = nodes.find_height(root.right)

        return left_height - right_height

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        return y


if __name__ == "__main__":
    myTree = AVLTree()
    root = TreeNode(10)
    root = myTree.insert_node(root, TreeNode(20))
    root = myTree.insert_node(root, TreeNode(30))
    root = myTree.insert_node(root, TreeNode(40))
    root = myTree.insert_node(root, TreeNode(50))
    root = myTree.insert_node(root, TreeNode(25))
    nodes.pre_order(root)
