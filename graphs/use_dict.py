graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['C'],
    'E': ['F'],
    'F': ['C']
}

graph_2 = {0: [1, 2], 1: [3], 2: [3], 3: []}


def find_path(graph, start, end, path=[]):
    """Determine a path without cycles between two nodes

    Takes graph, start, end nodes as arguments
    """
    path = path + [start]

    if start == end:
        return path

    if not graph.has_key(start):
        return None

    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)

            if new_path:
                return new_path

    return None


def find_all_paths(graph, start, end, path=[]):
    """Determine all paths without cycles between two nodes"""
    path = path + [start]

    if start == end:
        return [path]

    if not graph.has_key(start):
        return []

    paths = []

    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)

            for new_path in new_paths:
                paths.append(new_path)

    return paths


if __name__ == "__main__":
    print(find_path(graph, 'A', 'D'))
    print(find_all_paths(graph, 'A', 'D'))
    print(find_all_paths(graph_2, 0, 3))
