def preorder(tree):
    """Uses:
    1. Create a copy of the tree
    2. Create prefix expression on an expression tree
    """
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def postorder(tree):
    """
    Uses:

    1. Delete tree
    2. Get the postfix exporession of an expression tree
    """
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def inorder(tree):
    """
    Uses:

    For a BST gives nodes in increasing order
    """
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
