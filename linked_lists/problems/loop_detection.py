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


def get_intersect(head):
    """
    A fast pointer will either loop around a cycle and meet the slow
    pointer or reach the `null` at the end of a non-cyclic list.
    """
    slow = head
    fast = head

    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return slow

    return None


def loop_detection_floyd_cycle(head):
    """
    Traverse linked list using 2 pointers

    Move one pointer(slow) by one and another pointer by two(fast)
    If pointers meet at the same node, there is a loop. If pointers do
    not meet
    """
    if head is None:
        return None

    intersect = get_intersect(head)
    if intersect is None:
        return None
    # To find the entrance to the cycle, we have two pointers traverse at
    # the same speed -- one from the front of the list, and the other from
    # the point of intersection.
    ptr1 = head
    ptr2 = intersect

    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1
