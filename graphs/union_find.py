
"""
References:
https://www.youtube.com/watch?v=wU6udHRIkcc
https://youtu.be/eTaWFhPXPz4?t=476
https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
"""

from typing import List
import graph


def find_naive(parent_list: List[int], v: int) -> int:
    """Find the absolute root for a particular element"""
    if parent_list[v] == v:
        return v

    return find_naive(parent_list, parent_list[v])


def find_optmized(parent_list: List[int], v: int):
    """Find the absolute root by using the collapsing find method

    Gurantees that successive finds after the first find are optimized
    """
    if parent_list[v] == v:
        return v

    parent_list[v] = find_optmized(parent_list, parent_list[v])

    return parent_list[v]


def union_naive(parent_list: List[int], u: int, v: int) -> None:
    """Perform union on 2 disjoint sets

    Time complexity: O(n)
    """
    root_u = find_naive(parent_list, u)
    root_v = find_naive(parent_list, v)

    parent_list[root_u] = root_v


def union_optimized(parent_list: List[int], rank_list: List[int], u: int, v: int):
    """Perform union of 2 disjoint sets by rank

    Attach smaller rank tree under root of higher rank tree

    Time complexity: O(log n)
    """
    parent_u = find_optmized(parent_list, u)
    parent_v = find_optmized(parent_list, v)

    if rank_list[parent_u] > rank_list[parent_v]:
        parent_list[parent_v] = parent_u
        rank_list[parent_u] += rank_list[parent_v]

    elif rank_list[parent_v] > rank_list[parent_u]:
        parent_list[parent_u] = parent_v
        rank_list[parent_v] += rank_list[parent_u]

    else:
        # if roots are the same, mark one as root and
        # increment rank
        parent_list[parent_u] = parent_v
        rank_list[parent_v] += 1


def is_cyclic(number_of_vertices: int, graph: 'graph.Graph') -> bool:
    """Detect if there is a cycle in an undirected graph

    Assumes that the graph doesn't contain any self-loops
    """
    # An array to keep track of the subsets and which nodes,
    # belong that subset.
    # First create subsets containing a single node which are
    # the parent of itself
    parent_list = [i for i in range(number_of_vertices)]

    for u in graph:
        for v in graph[u]:
            root_u = find_naive(parent_list, u)
            root_v = find_naive(parent_list, v)
            # if two end nodes of an edge belongs to the
            # same set, then they form a cycle
            if root_u == root_v:
                return True

            union_naive(parent_list, root_u, root_v)

    return False
