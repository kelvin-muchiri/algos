class BinaryTree:
    """
    Tree implementation using nodes and references.
    Left and right will become references of other
    instances of the class
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
            r.rightChild = self.rightChild
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
