"""
Given the head of a linked list, return the node
where the cycle begins. If there is no cycle, return null.
"""


def loop_detection(head):
    """
    Attempted solution: uses hashtable

    Time complexity: O(n)
    Space complexity: O(n)
    """
    current = head
    nodes = set()

    while True:
        if current is None:
            # There is no loop exit
            break

        if current not in nodes:
            nodes.add(current)
            current = current.next

        else:
            # There is a loop return the node where
            # cycle begins
            return current

    return None
