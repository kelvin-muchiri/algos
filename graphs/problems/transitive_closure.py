from typing import List
import unittest


class Solution:
    def depth_first_traversal(self, N: int,  start_node: int, graph: List[List[int]], visited: List[bool], reachable: List[int]) -> None:
        visited[start_node] = True
        reachable.append(start_node)

        for neighbour in range(N):
            if graph[start_node][neighbour] and not visited[neighbour]:
                self.depth_first_traversal(
                    N, neighbour, graph, visited, reachable)

    def transitiveClosure(self, N, graph):
        closure = [[0 for j in range(N)] for i in range(N)]

        for node in range(N):
            reachable_nodes = []
            visited = [False for i in range(N)]

            self.depth_first_traversal(
                N, node, graph, visited, reachable_nodes)

            for reachable_node in reachable_nodes:
                closure[node][reachable_node] = 1

        return closure


class SolutionTestCase(unittest.TestCase):
    def test_works(self):
        sol = Solution()

        self.assertEqual(sol.transitiveClosure(
            4, [[1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]]), [[1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 1], [0, 0, 0, 1]])
        self.assertEqual(sol.transitiveClosure(
            3, [[0, 0, 0], [0, 0, 0], [0, 0, 0]]), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertEqual(sol.transitiveClosure(
            2, [[1, 1], [1, 1]]), [[1, 1], [1, 1]])


if __name__ == "__main__":
    unittest.main()
