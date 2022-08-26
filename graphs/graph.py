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
        """Visits each of a's neighbors before visiting any of their neighbors

        Time complexity: O(V + E) where V is the number of vertices and E
        is the number of edges in the graph
        Space comlexity: O(V) set of size V is needed

        Applications:

        1. Shortest path
        2. Peer to peer network
        3. Crawlers in search engine
        4. Social networking sites
        5. GPS Navigation systems - find all neighbouring locations
        6. Broadcasting in network - a broadcasted packet follows BFS to reach
        all nodes
        7. Garbage collection
        """
        # Mark all vertices as not visited
        visited = set()
        queue = []

        # mark the source node as visited and enqueue
        visited.add(src)
        queue.append(src)

        while queue:
            # dequeue a vertex from the queue and print it
            r = queue.pop(0)
            print(r, end=" ")

            # if an adjacent vertext has not been visited,
            # mark it as visited then enqueue it
            for i in self.graph[r]:
                if i not in visited:
                    visited.add(i)
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

        Time complexity: O(V + E) where V is the number of vertices and E
        is the number of edges in the graph
        Space comlexity: O(V) set of size V is needed

        Applications:

        1. Detecting cycle in graph
        2. Find if there is a path between 2 vertices
        3. Topological sorting
        4. Test if graph is biparite
        5. Finding strongly connected components of a graph - If there is a path
        from  each vertex to every other vertex
        6. Solving puzzles with only one solution - include
        only nodes on the current path in the visited set
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
