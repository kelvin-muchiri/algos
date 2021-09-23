"""
Given a binary tree, design an algorithm which creates a linked list of all
the nodes at each depth (e.g., if you have a tree with depth 0, you'll have 0 linked lists).
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, next):
        self.next = next


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, val):
        node = Node(val)
        node.set_next(self.head)
        self.head = node


def get_tree_lists(root):
    all_linked_lists = []

    if root:
        queue = []

        unordered_list = UnorderedList()
        queue.append({
            'list': unordered_list,
            'node': root
        })
        all_linked_lists.append(unordered_list)

        while queue:
            r = queue.pop(0)

            unordered_list = r['list']
            unordered_list.add(r['node'].get_root_value())

            if r['node'].left or r['node'].right:
                children_list = UnorderedList()
                all_linked_lists.append(children_list)

                if r['node'].left:
                    queue.append({
                        'list': children_list,
                        'node': r['node'].left
                    })

                if r['node'].right:
                    queue.append({
                        'list': children_list,
                        'node': r['node'].right
                    })

    return all_linked_lists


class TreeNode:
    """Just a tree node to test our code"""

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def get_root_value(self):
        return self.val

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(len(get_tree_lists(root)))
