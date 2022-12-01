"""
Given a pointer to the root of a binary tree, print the top view of the binary tree.

The tree as seen from the top the nodes, is called the top view of the tree.

Source:
https://www.hackerrank.com/challenges/tree-top-view/problem?isFullScreen=true

References:
https://www.youtube.com/watch?v=Et9OCDNvJ78&ab_channel=takeUforward
"""


def topView(root):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    queue = []
    queue.append([root, 0])
    top_view_map = {}

    while queue:
        item = queue.pop(0)
        node = item[0]
        horizontal_distance = item[1]

        if not top_view_map.get(horizontal_distance, None):
            top_view_map[horizontal_distance] = node.info

        if node.left:
            queue.append([node.left, horizontal_distance - 1])

        if node.right:
            queue.append([node.right, horizontal_distance + 1])

    for key in sorted(top_view_map):
        print(top_view_map[key], end=" ")
