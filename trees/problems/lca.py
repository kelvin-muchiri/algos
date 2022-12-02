"""
https://www.youtube.com/watch?v=gs2LMfuOR9k&ab_channel=NeetCode
https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem?isFullScreen=true
"""


def lca(root, v1, v2):
    current = root

    while current:
        if v1 > current.info and v2 > current.info:
            # go right
            current = current.right
        elif v1 < current.info and v2 < current.info:
            # go left
            current = current.left
        else:
            # split occurs here
            return current
