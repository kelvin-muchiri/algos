""""
Given a min heap, find the maximum element present in the heap.

https://www.geeksforgeeks.org/maximum-element-in-min-heap/
"""


def find_maximum_element(heap, n):
    """
    Returns maximum element in a min heap

    A min heap requires that the parent node be lesser than children node.
    Therefore, a non-leaf node cannot be the maximum element. We narrow
    our search only to leaf nodes, ceil(n/2)
    The time and space complexity remains O(n) as a constant factor of 1/2
    does not affect the asymptotic complexity.
    """
    max_element = heap[n // 2]

    for i in range(1 + n // 2, n):
        max_element = max(max_element, heap[i])

    return max_element
