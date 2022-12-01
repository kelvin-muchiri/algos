"""
If we can perform search on a sorted array in O(log n), and we can also perform
search in a BST in O(log n), then why would one choose a BST over an array?

Answer:
We consider the operations we would like to perform. The main operations
we would like to perform on a collection are

1. search
2. insert
3. delete

#### Sorted array ####

insert(x)
We can use binary search to search for the first element which is just greater than
x. However, we will have to shift elements greater than that position to the right.
Therefore the runtime will be  O(log n) + O(n) = O(n)

delete(x)
We can use binary search to search for x. After deletion, we'll have to shift elements
to the left. Hence the run time will be O(log n) + O(n) = O(n)

### Binary Search Tree ###
We can perform insert(x), search(x), delete(x) all in O(log n) in average case. In worst
case, the cost is O(n) which occurs if a tree is not balanced. We can avoid the worst
case by making sure that the tree is always balanced.

BST gets unbalance during insertion and deletion. So after insertion or deletion, we
should rebalance

References:
https://www.youtube.com/watch?v=pYT9F8_LFTM
"""
import math


class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


def insert_node(root, node):
    """Insert node recursively"""
    if root is None:
        root = node
    else:
        if node.data <= root.data:
            if root.left is None:
                root.left = node
            else:
                root.left = insert_node(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                root.right = insert_node(root.right, node)
    return root


def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.data)
        in_order_traversal(root.right)


def search(root, data):
    if root is None:
        return False

    if root.data == data:
        return True

    if data <= root:
        return search(root.left, data)

    return search(root.right, data)


def find_min(root):
    if root is None:
        return -1

    if root.left is None:
        return root.data

    return find_min(root.left)


def find_min_value_node(root):
    if root is None or root.left is None:
        return root

    return find_min_value_node(root.left)


def find_max(root):
    if root is None:
        return -1

    if root.right is None:
        return root.data

    return find_max(root.right)


def is_binary_search_tree_util(root, min_val, max_val):
    if root is None:
        return True

    return root.data > min_val and root.data < max_val and \
        is_binary_search_tree_util(root.left, min_val, root.data) and \
        is_binary_search_tree_util(root.right, root.data, max_val)


def is_binary_search_tree(root):
    """
    Check if is BST

    Time complexity: O(n)

    You can also use in order traversal
    https://www.youtube.com/watch?v=yEwSGhSsT0U&ab_channel=mycodeschool"""
    return is_binary_search_tree_util(root, -math.inf, math.inf)


def delete_node(root, data):
    """Delete a node from a binary search tree

    https://www.youtube.com/watch?v=gcULXE7ViZw&ab_channel=mycodeschool
    """
    if root is None:
        return root

    if data < root.data:
        # narrow search space to the left subtree
        root.left = delete_node(root.left, data)

    elif data > root.data:
        # narrow search space to right subtree
        root.right = delete_node(root.right, data)

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
            min_right_node = find_min_value_node(root.right)
            root.data = min_right_node.data
            root.right = delete_node(root.right, min_right_node.data)

    return root


if __name__ == "__main__":
    r = TreeNode(55)
    insert_node(r, TreeNode(35))
    insert_node(r, TreeNode(25))
    insert_node(r, TreeNode(45))
    insert_node(r, TreeNode(75))
    insert_node(r, TreeNode(65))
    insert_node(r, TreeNode(85))
    in_order_traversal(r)

    print(is_binary_search_tree(r))
