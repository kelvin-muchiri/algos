from data_structures.stack import Stack
from trees.nodes import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        
        elif i == ')':
            currentTree == pStack.pop()

        else:
            # Raise an error if we get a token in the list that
            # we don't recognize
            raise ValueError
    
    return eTree

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
pt.postorder()



