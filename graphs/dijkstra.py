"""
Dijkstras algorithm for finding the shortest path from source vertex to every other vertex.

f we are interested only in the shortest distance from the source to a single target,
break them for a loop when the picked minimum distance vertex is equal to the target.

Algorithm works for both directed and undirectd graphs

References:
https://www.youtube.com/watch?v=pVfj6mxhdMw
https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
"""


import math
from typing import List, Optional, Dict
import unittest


class Solution:
    def get_next_node(self, visited: List[bool], distances: Dict[int, int]) -> Optional[int]:
        """Returns the unvisited node with smallest known distance from start node"""
        current_node = None

        for node in range(len(visited)):
            if not visited[node]:
                if current_node is None:
                    current_node = node
                    continue

                if distances[node] < distances[current_node]:
                    current_node = node

        return current_node

    def relax_node_distance(self, node: int, parent: int, distances: Dict[int, int], weight: int, previous: List[int]) -> None:
        """Relax a node's distance"""
        # distance of parent node + weight from parent to node
        new_distance = distances[parent] + weight

        if new_distance < distances[node]:
            distances[node] = new_distance
            previous[node] = parent

    def process_node(self, node: int, adj: List[List[int]], visited: List[bool], distances: Dict[int, int], previous: List[int]) -> None:
        """Visit node and relax the distances its unvisited neighbours"""
        visited[node] = True

        for neighbour in adj[node]:
            if not visited[neighbour[0]]:
                self.relax_node_distance(neighbour[0], node, distances,
                                         neighbour[1], previous)

    def get_unvisited(self, visited: List[bool]):
        """Get unvisited nodes"""
        unvisited = []

        for i in range(len(visited)):
            if not visited[i]:
                unvisited.append(i)

        return unvisited

    # Function to find the shortest distance of all the vertices
    # from the source vertex S.

    def dijkstra(self, V, adj, S):
        # distance of every node from start node
        distances = [math.inf for i in range(V)]
        distances[S] = 0
        visited = [False for i in range(V)]
        previous = [-1 for i in range(V)]

        self.process_node(S, adj, visited, distances, previous)

        while self.get_unvisited(visited):
            self.process_node(self.get_next_node(visited, distances), adj, visited,
                              distances, previous)

        return distances


class SolutionTestCase(unittest.TestCase):
    def test_solution(self):
        sol = Solution()
        self.assertEqual(sol.dijkstra(2, [[[1, 9]], [[0, 9]]], 0), [0, 9])
        self.assertEqual(sol.dijkstra(
            6, [[[3, 9], [5, 4]], [[4, 4]], [[5, 10]], [[0, 9]], [[5, 3], [1, 4]], [[0, 4], [2, 10]]], 1), [11, 0, 17, 20, 4, 7])


if __name__ == "__main__":
    unittest.main()
