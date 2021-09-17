"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""

import unittest

from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def is_there_route_between(self, src, dest):
        """Given two nodes, return true if there is a route between them false otherwise

        Uses breadth first search"""
        # Mark all the vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue
        visited[src] = True
        queue.append(src)

        while queue:
            # Dequeque
            r = queue.pop(0)

            # if this adjacent node is the destination node, return true
            if r == dest:
                return True

            # if an adjacent vertext has not been visited,
            # mark it as visited then enqueue it
            for i in self.graph[r]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)

        return False


class SolutionTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()

        self.graph = Graph()
        self.graph.add_edge(0, 1)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 1)
        self.graph.add_edge(2, 0)
        self.graph.add_edge(3, 2)
        self.graph.add_edge(4, 5)
        self.graph.add_edge(5, 4)

    def test_0_1(self):
        self.assertTrue(self.graph.is_there_route_between(0, 1))

    def test_0_4(self):
        self.assertFalse(self.graph.is_there_route_between(0, 4))


if __name__ == "__main__":
    unittest.main()
