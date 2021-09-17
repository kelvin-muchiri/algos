"""
Python program to represent the adjacency list representation of the graph
"""
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, src, dest):
        self.graph[src].append(dest)

    def breath_first_search(self, src):
        """Visits each of a's neighbors before visiting any of their neighbors"""
        # Mark all vertices as not visited
        visited = [False] * (max(self.graph) + 1)

        queue = []

        # mark the source node as visited and enqueue
        visited[src] = True
        queue.append(src)

        while queue:
            # dequeue a vertex from the queue and enqueue it
            r = queue.pop(0)
            print(r, end=" ")

            # if an adjacent vertext has not been visited,
            # mark it as visited then enqueue it
            for i in self.graph[r]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)

    def _depth_first_search(self, src, visited):
        # mark the source node as visited
        print(src, end=" ")
        visited.add(src)

        for i in self.graph[src]:
            if i not in visited:
                self._depth_first_search(i, visited)

    def depth_first_search(self, src):
        """
        When visiting a node b that is a neighbor of a, we visit all of b's neighbors
        before going on to a's other neighbors.
        """
        visited = set()

        self._depth_first_search(src, visited)


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    print('BFS')
    graph.breath_first_search(2)
    print('DFS')
    graph.depth_first_search(2)
