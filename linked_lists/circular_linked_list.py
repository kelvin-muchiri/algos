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

from linked_lists.node import Node


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
        node = Node(data)
        node.set_next(self.tail.get_next())
        self.tail.set_next(node)

    def append(self, data):
        """Add a new item to the end of the list"""
        node = Node(data)
        node.set_next(self.tail.get_next())
        self.tail.set_next(node)
        self.tail = node

    def insert(self, pos, data):
        """
        Adds a new item to the list at position pos. Assumption is that
        item is not in the list, and there are enought items to have
        position pos
        """
