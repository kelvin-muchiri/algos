#!/bin/python3

from heapq import heapify, heappop, heappush
import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


class MinIntHeap:
    def __init__(self):
        self.items = []
        self.size = 0

    def get_parent_index(self, childIndex):
        return (childIndex - 1) // 2

    def get_left_child_index(self, parentIndex):
        return (parentIndex * 2) + 1

    def get_right_child_index(self, parentIndex):
        return (parentIndex * 2) + 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def get_parent(self, childIndex):
        return self.items[self.get_parent_index(childIndex)]

    def get_left_child(self, parentIndex):
        return self.items[self.get_left_child_index(parentIndex)]

    def get_right_child(self, parentIndex):
        return self.items[self.get_right_child_index(parentIndex)]

    def peek(self):
        return self.items[0]

    def poll(self):
        item = self.items[0]

        if self.size == 1:
            self.items = []
        else:
            self.items[0] = self.items.pop()

        self.size -= 1
        self.heapify_down()
        return item

    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self.heapify_up()

    def heapify_up(self):
        index = self.size - 1

        while self.has_parent(index) and \
                self.get_parent(index) > self.items[index]:
            swap(index, self.get_parent_index(index), self.items)
            index = self.get_parent_index(index)

    def heapify_down(self):
        index = 0
        self._heapify_down_util(index)

    def _heapify_down_util(self, index):
        stop = False

        while self.has_left_child(index) and not stop:
            smaller_child_index = self.get_left_child_index(index)

            if self.has_right_child(index) and \
                    self.get_right_child(index) < self.get_left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self.items[index] <= self.items[smaller_child_index]:
                stop = True
            else:
                swap(index, smaller_child_index, self.items)

            index = smaller_child_index

    def heapify(self, initial_array):
        self.size = len(initial_array)
        self.items = initial_array.copy()
        parent_index_of_last_node = self.get_parent_index(
            len(initial_array) - 1)
        i = parent_index_of_last_node

        while i >= 0:
            self._heapify_down_util(i)

            i -= 1

        return self.items


def cookies(k, A):
    heapify(A)

    if len(A) == 0:
        return -1

    iterations = 0

    while A[0] < k and len(A) > 1:
        least_min = heappop(A)
        second_least_min = heappop(A)
        heappush(A, least_min + 2 * second_least_min)
        iterations += 1

    if len(A) == 1:
        if A[0] >= k:
            return iterations
        else:
            return -1

    return iterations


def cookies_custom_heap(k, A):
    if len(A) == 0:
        return -1

    min_heap = MinIntHeap()
    min_heap.heapify(A)
    iterations = 0

    while min_heap.peek() < k and min_heap.size > 1:
        least_min = min_heap.poll()
        second_least_min = min_heap.poll()
        min_heap.insert(least_min + 2 * second_least_min)
        iterations += 1

    if min_heap.size == 1:
        if min_heap.peek() >= k:
            return iterations
        else:
            return -1

    return iterations


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
