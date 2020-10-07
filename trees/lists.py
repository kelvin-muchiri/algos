""" myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
print(myTree)
print('left subtree = ', myTree[1])
print('root = ', myTree[0])
print('right subtree = ', myTree[2])
 """

def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    """
    First obtain the list (possibly empty) that corresponds to the
    current left child. We add the new left child
    installing the old left child as the left child
    of the new one
    """
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    
    else:
        root.insert(1, [newBranch, [], []])

def insertRight(root, newBranch):
    """
    First obtain the list (possibly empty) that corresponds to the
    current right child. We add the new right child installing 
    the right child as the right child of the new one
    """
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    
    else:
        root.insert(2, [newBranch, [], []])


def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]


r = BinaryTree(3)
print(r)
insertLeft(r, 4)
print(r)
insertLeft(r, 5)
print(r)
insertRight(r, 6)
print(r)
insertRight(r, 7)
print(r)
l = getLeftChild(r)
print(l) 
setRootVal(l, 9)
print(r)
insertLeft(l, 11)
print(r)

"""
print(getRightChild(getRightChild(r))) """
