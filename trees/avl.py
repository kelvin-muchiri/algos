"""
When creating a BST, we want to create a BST with the minimal height

An AVL tree is a self balancing binary tree where the
balance factor = height of left subtree - height of right subtree {-1, 0, 1}. This
must be true for all nodes

If a node say has a balance factor of 2, then it is heavy on the left side. If the
balance factor of -2, then it is heavy of the right side

Rotations are always done within 3 nodes (x, y, z)

https://www.youtube.com/watch?v=jDM6_TnYIqE&ab_channel=AbdulBari
https://www.geeksforgeeks.org/insertion-in-an-avl-tree/
https://www.youtube.com/watch?v=kD_xn7mZ6v8&ab_channel=LalithaNatraj
https://www.geeksforgeeks.org/deletion-in-an-avl-tree/
"""
import nodes
import bst


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    """Self balancing AVL BST"""

    def insert_node(self, root, node):
        """Insert node into an AVL"""
        # normal BST insert
        if root is None:
            root = node
        else:
            if node.data <= root.data:
                if root.left is None:
                    root.left = node
                else:
                    root.left = self.insert_node(root.left, node)
            else:
                if root.right is None:
                    root.right = node
                else:
                    root.right = self.insert_node(root.right, node)

        # Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))
        # get the balance factor
        balance_factor = self.get_balance_factor(root)

        # Case 1 - Left Left imbalance (RR)
        if balance_factor > 1 and node.data < root.left.data:
            return self.right_rotate(root)

        # Case 2 - Right Right imbalance (LL)
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

    def delete_node(self, root, data):
        """Delete node from AVL tree, returns root of modified subtree

        Unlike insertion, in deletion, after we perform a rotation at z,
        we may have to perform a rotation at ancestors of z. Thus, we must
        continue to trace the path until we reach the root.
        """
        # perform standard BST delete
        if root is None:
            return root

        if data < root.data:
            # narrow search space to the left subtree
            root.left = self.delete_node(root.left, data)

        elif data > root.data:
            # narrow search space to right subtree
            root.right = self.delete_node(root.right, data)

        elif data == root.data:
            # node found

            # case 1: No child
            if root.left is None and root.right is None:
                root = None
            # case 2: One child, has right child only
            elif root.left is None:
                root = root.right  # replace root with right child

            # case 3: One child, has left child only
            elif root.right is None:
                root = root.left  # replace root with left child

            # case 4: Has 2 children
            else:
                min_right_node = bst.find_min_value_node(root.right)
                root.data = min_right_node.data
                root.right = self.delete_node(root.right, min_right_node.data)

        # If the tree has only one node,
        # simply return it
        if root is None:
            return root

        # Update the height of the ancestor node
        root.height = 1 + max(self.get_height(root.left),
                              self.get_height(root.right))

        # Step 3 - Get the balance factor
        balance_factor = self.get_balance_factor(root)

        # Case 1 - Left Left
        if balance_factor > 1 and self.get_balance_factor(root.left) >= 0:
            return self.right_rotate(root)

        # Case 2 - Right Right
        if balance_factor < -1 and self.get_balance_factor(root.right) <= 0:
            return self.left_rotate(root)

        # Case 3 - Left Right
        if balance_factor > 1 and self.get_balance_factor(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Case 4 - Right Left
        if balance_factor < -1 and self.get_balance_factor(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def get_balance_factor(self, root):
        """Get the balance factor"""
        if root is None:
            return 0

        return self.get_height(root.left) - self.get_height(root.right)

    def get_height(self, root):
        if root is None:
            # height of external (nil) nodes is 0
            return 0

        return root.height

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left),
                           self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))

        return y


if __name__ == "__main__":
    myTree = AVLTree()
    root = TreeNode(10)
    root = myTree.insert_node(root, TreeNode(20))
    root = myTree.insert_node(root, TreeNode(30))
    root = myTree.insert_node(root, TreeNode(40))
    root = myTree.insert_node(root, TreeNode(50))
    root = myTree.insert_node(root, TreeNode(25))
    print("Preorder Traversal after insertion -")
    nodes.pre_order(root)
    myTree.delete_node(root, 40)
    print("Preorder Traversal after deletion -")
    nodes.pre_order(root)
