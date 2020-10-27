class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.head.next = self.tail
        self.tail.next = self.head
