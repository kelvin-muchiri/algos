""""
Heaps

parent = (index - 1) / 2
left = index * 2 + 1
right = index * 2 + 2

Operations on Heap:
1. Heapify
2. Insertion
3. Deletion
4. Peek

Applications:
1. Construct a priority queue
2. Heap sort - O (n log n)
    Step 1: Create a max heap
    Step 2: Delete all elements one by one (remember the root is always
            the first to be deleted. This will create an array sorted in ascending order).
            https://youtu.be/HqPJF2L5h9U?t=1903

Real time applications:
1. Patient treatment in a hospital. Patient with more injury is treated first. Priority is the
degree of injury
2. System concerned with security use heap sort e.g Linux Kernel

Advantages:
1. Inserting and deletion in just O(log n). When using an array as a priority queue, insertion and
deletion will take O(n) (https://youtu.be/HqPJF2L5h9U?t=2951). Hence, heap is the best data structure
for implementing priority queues
2. Finding the greatest number or minimum number in O(1)
3. Can be implemented using an array. Doesn't need an extra space for a pointer
4. A balanced binary tree that is easy to implement
5. Heap can be created in O(n)

Disadvantages:
1. Searching an element takes O(n)
2. Finding a successor or predecessor takes O(n), while for a BST takes O(log n)
3. Print elements in sorted order takes O(n * log n), while for a BST takes O(n)

References:
https://www.youtube.com/watch?v=t0Cq6tVNRBA&ab_channel=HackerRank
https://www.geeksforgeeks.org/applications-advantages-and-disadvantages-of-heap/
https://www.youtube.com/watch?v=HqPJF2L5h9U&ab_channel=AbdulBari
"""
import unittest


def swap(i, j, array):
    """Swap the values of two indices"""
    array[i], array[j] = array[j], array[i]


class MinIntHeap:
    def __init__(self):
        # heap items
        self.items = []
        # Keep track of the size of the heap
        self.size = 0

    def get_left_child_index(self, parentIndex):
        """Return left child index"""
        return parentIndex * 2 + 1

    def get_right_child_index(self, parentIndex):
        """Return right child index"""
        return parentIndex * 2 + 2

    def get_parent_index(self, childIndex):
        """Return parent index"""
        return (childIndex - 1) // 2

    def has_left_child(self, index):
        """Check if has left child"""
        return self._has_left_child(index, self.size)

    def _has_left_child(self, index, array_size):
        return self.get_left_child_index(index) < array_size

    def has_right_child(self, index):
        """Check if has right child"""
        return self._has_right_child(index, self.size)

    def _has_right_child(self, index, array_size):
        return self.get_right_child_index(index) < array_size

    def has_parent(self, index):
        """Check if has parent"""
        return self.get_parent_index(index) >= 0

    def get_left_child(self, index):
        """Get left child"""
        return self.items[self.get_left_child_index(index)]

    def get_right_child(self, index):
        """Get right child"""
        return self.items[self.get_right_child_index(index)]

    def get_parent(self, index):
        """Get parent"""
        return self.items[self.get_parent_index(index)]

    def peek(self):
        """Get the most minum element"""
        # min element will always be the root of the heap
        if self.size == 0:
            raise Exception('Heap is empty')

        return self.items[0]

    def poll(self):
        """"Get the minium element and remove from heap

        Swap with last element (bottommost, rightmost). Bubbledown
        until we find its appropriate

        Time Complexity: O(log n), proportional to the height of the tree
        """
        if self.size == 0:
            raise Exception('Heap is empty')

        item = self.items[0]
        self.items[0] = self.items.pop()
        self.size -= 1
        self.heapfiy_down()
        return item

    def add(self, item):
        """Insert to heap

        Add as the last element (bottommost, rightmost). Bubble up until
        min heap property is restored

        Time Complexity: O(log n), proportional to the height of the tree
        """
        self.items.append(item)
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        """
        Bubble up last element, swapping with its parent until min heap property
        is restored
        """
        index = self.size - 1

        while self.has_parent(index) and self.get_parent(index) > self.items[index]:
            swap(index, self.get_parent_index(index))
            index = self.get_parent_index(index)

    def heapify_down(self):
        """
        Bubble down top element, swapping with one of its children until
        min heap property is restored
        """
        self._heapify_down(0, self.items, self.size)

    def _heapify_down_util(self, index, array, heap_size):
        stop = False

        # we only check for left child since if no left child, right child
        # is not present (remember heap is filled from top-bottom then left-right)
        while self._has_left_child(index, heap_size) and not stop:
            smaller_child_index = self.get_left_child_index(index)

            if self._has_right_child(index, heap_size) and \
                    array[self.get_right_child_index(index)] < array[self.get_left_child_index(index)]:
                smaller_child_index = self.get_right_child_index(index)

            if array[index] < array[smaller_child_index]:
                stop = True
            else:
                swap(index, smaller_child_index, array)

            index = smaller_child_index

    def build(self, initial_array):
        """Build heap from an array of integers

        Build by adding each element as the last element then bubbling up the element
        to find its position. Elements are inserted from left - right in the heap array

        Time complexity: O(n log n)
        """

        for i in range(len(initial_array)):
            self.add(initial_array[i])

        return self.items

    def heapify(self, initial_array):
        """Build heap from an array of integers

        Start from right to left and for each element, bubble down element until
        min heap property

        Ref: https://youtu.be/HqPJF2L5h9U?t=2666

        Time complexity: O(n)
        """
        i = len(initial_array) - 1
        items = initial_array.copy()

        while i >= 0:
            self._heapify_down_util(i, items, len(items))
            i -= 1

        self.items = items

        return self.items


class MinIntHeapTestCase(unittest.TestCase):
    """Tests for MinIntHeap"""

    def test_build(self):
        """Building a min heap works"""
        heap = MinIntHeap()
        heap.build([10, 20, 15, 30, 40])
        self.assertEqual(heap.items, [10, 20, 15, 30, 40])

    def test_heapify(self):
        """Building a min heap works"""
        heap = MinIntHeap()
        heap.heapify([10, 20, 15, 30, 40])
        self.assertEqual(heap.items, [10, 20, 15, 30, 40])


if __name__ == "__main__":
    unittest.main()
