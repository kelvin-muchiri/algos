"""
All Paths From Source to Target
"""


class Solution:
    def allPathsSourceTarget(self, graph):
        # Build the adjacency list
        graph_dict = {}

        for i in range(len(graph)):
            graph_dict[i] = graph[i]
        print('Graph', graph_dict)
        return self.find_all_paths(graph_dict, 0, len(graph) - 1)

    def find_all_paths(self, graph, start, end, path=[]):
        """Determine all paths without cycles between two nodes"""
        path = path + [start]

        if start == end:
            return [path]

        if not start in graph:
            return []

        paths = []

        for node in graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(graph, node, end, path)

                for new_path in new_paths:
                    paths.append(new_path)

        return paths
