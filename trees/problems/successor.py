""""
Write an algorithm to find the "next" node (i.e., in-order successor)
of a given node in a binary search tree. You may assume that each node has a link to its parent.
"""


class Solution:
    """Attempted solution

    Time complexity: O(h) where h is the height of the tree
    Space complexity: O(1)
    """
    # returns the inorder successor of the Node x in BST (rooted at 'root')

    def inorderSuccessor(self, root, x):
        # Code here
        return self.inorder(x, root)

    def inorder(self, needle, root):
        if root is None:
            return None

        successor = self.inorder(needle, root.left)

        if successor:
            return successor

        if root.data > needle.data:
            return root

        return self.inorder(needle, root.right)
