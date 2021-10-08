"""
All nodes are connected to form a circle. There is no NULL
at the end. Can be a singly or doubly

1. Any node can be a starting  point. We can traverse the whole list from
any point. Just stop when the first node is visited again.

2. Useful for queue implementation. Only one pointer is required, rear.
Front can always be obtained as next of last

3. When multiple applications are running on a PC, it is common
for the operating system to put the running applications on a list and then
to cycle through them, giving each of them a slice of time to execute

4. Implementation of advanced data structures e.g Fibonacci Heap

Ref:
https://www.geeksforgeeks.org/circular-linked-list/
"""

import unittest


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class CircularLinkedList:
    def __init__(self):
        self.tail = None  # pointer to the last node,
        # insertion to the beginning and end takes constant time

    def add_to_empty(self, data):
        node = Node(data)
        self.tail = node
        node.set_next(self.tail)

    def add_to_beginning(self, data):
        """Add a new item to the beginning of a list"""
        if self.tail is None:
            self.add_to_empty(data)

        else:
            node = Node(data)
            node.set_next(self.tail.get_next())
            self.tail.set_next(node)

        return self.tail

    def append(self, data):
        """Add a new item to the end of the list"""
        if self.tail is None:
            self.add_to_empty(data)

        else:
            node = Node(data)
            node.set_next(self.tail.get_next())
            self.tail.set_next(node)
            self.tail = node

        return self.tail

    def size(self):
        """Returns the number of items in the list"""
        if self.tail is None:
            return 0

        if self.tail.get_next() == self.tail:
            return 1

        count = 1  # we have counted tail
        current = self.tail.get_next()

        while current != self.tail:
            count += 1
            current = current.get_next()

        return count

    def insert(self, pos, data):
        """
        Adds a new item to the list at position pos. Assumption is that
        item is not in the list, and there are enought items to have
        position pos
        """

        if pos == 0:
            return self.add_to_beginning(data)

        if pos == self.size() - 1:
            return self.append(data)

        count = 1  # start at index 1
        current = self.tail.get_next().get_next()  # node at index 1
        previous = self.tail.get_next()

        while count <= pos:
            if count == pos:
                node = Node(data)
                node.set_next(previous.get_next())
                previous.set_next(node)

            else:
                current = current.get_next()
                previous = current

            count += 1

    def get_values(self):
        """Return all node values"""
        values = []
        current = self.tail.get_next()

        while current != self.tail:
            values.append(current.get_data())
            current = current.get_next()

        values.append(self.tail.get_data())

        return " ".join(map(str, values))


class CircularLinkedListTestCase(unittest.TestCase):
    def test_get_values(self):
        clist = CircularLinkedList()

        clist.add_to_empty(6)
        clist.add_to_beginning(4)
        clist.add_to_beginning(2)
        clist.append(8)
        clist.append(12)
        clist.insert(3, 10)

        self.assertEqual(clist.get_values(), "2 4 6 8 10 12")


if __name__ == "__main__":
    unittest.main()
