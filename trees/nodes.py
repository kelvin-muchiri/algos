"""
Tree implementation using nodes and references.
Left and right will become references of other
instances of the class

### BINARY SEARCH TREE
A binary search tree is a binary tree in which every node fits a specific
ordering property: all left descendents <= n < all right descendents.
This must be true for each node n.

The definition of a binary search tree can vary slightly with respect to equality.
Under some defi- nitions, the tree cannot have duplicate values. In others,
the duplicate values will be on the right or can be on either side.
All are valid definitions, but you should clarify this with your interviewer.

When give a question, many candidates assume the interviewer means a BST
Be sure to ask

### BALANCED VS UNBALANCED TREES
A balanced tree does not mean the left & right subtrees are exactly the same
size like you see under a perfect binary tee. A "balanced" tree really means
something more like "not terribly imbalanced".'
It's balanced enough to ensure O(log n) times for insert and find, but it's not
necessarily as balanced as it could be.

### COMPLETE BINARY TREES
Every level of the tree is fully filled except for perhaps the last level. To the
extent that the last level is filled, it is filled left to right

### FULL BINARY TREES
Every node has 0 or 2 children

### PERFECT BINARY TREES
Both full and complete

Note: Perfect trees are rare in interviews and in real life, as a perfect tree must
have excactly 2^k - 1 nodes, where k is the no. of levels. Do not assume  a binary tree is perfect
"""


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order(node):
    """Visit the left branch, then the current node, then right branch.
    For a BST, visit the nodes in ascending order hence the name
    in order"""

    if node:
        in_order(node.left)
        print(node.data)
        in_order(node.right)


def pre_order(node):
    """Visit the root node first, then left, then right.
    Visit the current node before its children nodes hence the name pre-order."""

    if node:
        print(node.data)
        pre_order(node.left)
        pre_order(node.right)


def post_order(node):
    """Visit the left branch, then the right, then the root.
    Visit the current node after its children nodes hence the name post-order."""
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data)


def breadth_first_traversal(root):
    """Level order traversal

    Time complexity: O(n)
    Space complexity: O(1) for skewed tree (only one element will be
    in the queue at a time), O(n) for balanced tree
    """
    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)

        print(node.data, end="")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


def find_height(root):
    """The max of the height of left and right subtrees plus 1
    https://www.youtube.com/watch?v=_pnqMz5nrRs&ab_channel=mycodeschool

    Time complexity: O(n)
    """
    if root is None:
        return -1

    left_height = find_height(root.left)
    right_height = find_height(root.right)

    return max(left_height, right_height) + 1
