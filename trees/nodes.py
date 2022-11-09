class BinaryTree:
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

    def __init__(self, rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        """
        If no left child, just add node to tree,
        else if there is an existing left child,
        push the existing child one level in the
        tree
        """
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        """
        if no right child, just insert node,
        else push existing child one level down
        """
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)

        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
print(r.getRootVal())

r.insertLeft('b')
print(r.getLeftChild().getRootVal())

r.insertRight('c')
print(r.getRightChild().getRootVal())

r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())


def in_order(node):
    """Visit the left branch, then the current node, then right branch.
    For a BST, visit the nodes in ascending order hence the name
    in order"""

    if node:
        in_order(node.getLeftChild())
        print(node.getRootVal())
        in_order(node.getRightChild())


def pre_order(node):
    """Visit the root node first, then left, then right.
    Visit the current node before its children nodes hence the name pre-order."""

    if node:
        print(node.getRootVal())
        pre_order(node.getLeftChild())
        pre_order(node.getRightChild())


def post_order(node):
    """Visit the left branch, then the right, then the root.
    Visit the current node after its children nodes hence the name post-order."""
    if node:
        post_order(node.getLeftChild())
        post_order(node.getRightChild())
        print(node.getRootVal())
