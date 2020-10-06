"""
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
"""

import unittest


class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None

    def get_vertex(self):
        return self.vertex

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # size of the array will be equal to the number of the vertices
        self.graph = [None] * self.V

    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

    # Function to print the graph
    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

    def is_there_route_between(self, src, dest):
        """Given two nodes, return true if there is a route between them false otherwise

        Uses breadth first search"""
        # Mark all the vertices as not visited
        visited = [False]*(self.V)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue
        visited[src] = True
        queue.append(src)

        while queue:
            # Dequeque
            n = queue.pop(0)

            # if this adjacent node is the destination node, return true
            if n == dest:
                return True

            # Else continue to do BFS
            temp = self.graph[n]

            while temp:
                if not visited[temp.vertex]:
                    queue.append(temp.vertex)
                    visited[temp.vertex] = True

                temp = temp.next

        return False


class SolutionTestCase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        V = 5
        self.graph = Graph(V)
        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 4)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(1, 4)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(3, 4)

    def test_0_1(self):
        self.assertTrue(self.graph.is_there_route_between(0, 1))

    def test_2_3(self):
        self.assertTrue(self.graph.is_there_route_between(2, 3))

    def test_3_2(self):
        self.assertFalse(self.graph.is_there_route_between(3, 2))

    def test_0_2(self):
        self.assertTrue(self.graph.is_there_route_between(0, 2))

    def test_0_3(self):
        self.assertTrue(self.graph.is_there_route_between(0, 3))


if __name__ == "__main__":
    unittest.main()
