""""
You are given a list of projects and a list of dependencies (which is a list of pairs of projects,
where the second project is dependent on the first project).
All of a project's dependencies must be built before the project is.
Find a build order that will allow the projects to be built.
If there is no valid build order, return an error.
"""
from collections import defaultdict


class Graph:
    """
    Solution: Topological sort

    This problem is called topological sort: linearly ordering
    the vertices in a graph such that for every edge (a, b), a
    appears before b in the linear order.

    Ref:

    https://www.geeksforgeeks.org/topological-sorting/

    Time complexity: O (P + D) where P is the number of projects and
    D the number of dependency pairs
    Space complexityL: O(P)
    """

    def __init__(self, vertices):
        self.graph = defaultdict(list)

    def add_edge(self, src, des):
        self.graph[src].append(des)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = set()
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in self.graph:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order
        # so as to print from top to bottom
