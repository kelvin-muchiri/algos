"""
Write code to remove duplicates from an unsorted linked list.
"""

import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val

    def set_next(self, node):
        self.next = node

    def get_next(self):
        return self.next


class UnorderedList:
    def __init__(self):
        self.head = None

    def get_head():
        return self.head

    def add(self, value):
        """Add node at the beginning"""
        node = Node(value)
        node.set_next(self.head)
        self.head = node

    def get_values(self):
        """Return all node values"""
        values = []
        current = self.head

        while current != None:
            values.append(current.get_val())
            current = current.get_next()

        return ",".join(map(str, values))


def remove_duplicates(head):
    """Remove duplicates from unordered list"""
    current = head
    previous = None
    unique = set()

    while current != None:
        if current.get_val() not in unique:
            unique.add(current.get_val())
            previous = current

        else:
            # it's a duplicate, detach node
            previous.set_next(current.get_next())

        current = current.get_next()

    return head


class UnorderedListTestCase(unittest.TestCase):
    def test_values(self):
        unordered_list = UnorderedList()
        unordered_list.add(4)
        self.assertEqual(unordered_list.get_values(), '4')
        unordered_list.add(1)
        self.assertEqual(unordered_list.get_values(), '1,4')


if __name__ == "__main__":
    unittest.main()
