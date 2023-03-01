"""
Problem: https://leetcode.com/problems/is-graph-bipartite/solutions/

References:
https://www.youtube.com/watch?v=-SpTh4AEZrk
https://www.geeksforgeeks.org/bipartite-graph/
"""


from typing import List


def isBipartiteBFS(self, graph: List[List[int]]) -> bool:
    """
    Time complexity: O(V + E)
    Auxiliary space: O(V)
    """
    num_vertices = len(graph)
    vertex_colors: List[int] = [-1 for i in range(num_vertices)]

    def bfs(source_node: int):
        # Assign first color to source
        vertex_colors[source_node] = 0
        queue = []
        queue.append(source_node)

        while queue:
            node = queue.pop()

            for neighbor in graph[node]:
                # if neighbor already colored same color as parent, bipartite is not
                # possible
                if vertex_colors[node] == vertex_colors[neighbor]:
                    return False

                if vertex_colors[neighbor] == -1:
                    # assign alternate color to neighbor
                    if vertex_colors[node] == 0:
                        vertex_colors[neighbor] = 1
                    else:
                        vertex_colors[neighbor] = 0

                    queue.append(neighbor)

        # all adjacent vertices can be colored with alternate color
        return True

    for node in range(num_vertices):
        if vertex_colors[node] == -1:
            if not bfs(node):
                return False

    return True


def isBipartiteUnionFind(self, graph: List[List[int]]) -> bool:
    number_of_vertices = len(graph)
    parent = [i for i in range(number_of_vertices)]
    rank = [1 for i in range(number_of_vertices)]

    def find_operation(node: int) -> int:
        if parent[node] == node:
            return node

        parent[node] = find_operation(parent[node])

        return parent[node]

    def union_operation(u: int, v: int) -> None:
        root_u = find_operation(u)
        root_v = find_operation(v)

        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
            rank[root_u] += rank[root_v]
        else:
            parent[root_u] = root_v
            rank[root_v] += rank[root_u]

    for node in range(number_of_vertices):
        neighbors = graph[node]

        for neighbor in neighbors:
            if find_operation(node) == find_operation(neighbor):
                return False

            # peform union on neighor and the first neighbor
            union_operation(neighbors[0], neighbor)

    return True
