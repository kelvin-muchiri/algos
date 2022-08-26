from linked_lists.node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        """
        Returns if the list is empty
        """
        return self.head == None

    def add(self, item):
        """
        Add item to list. We know we have found the place when we run
        out of nodes or the current node becomes greater than the
        item we wish to add
        """
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

        temp = Node(item)
        if previous == None:
            # Only one item in the list, perform an add, add
            # to the beginning of the list

            temp.set_next(self.head)
            self.head = temp

        else:
            temp.set_next(current)
            previous.set_next(temp)

    def size(self):
        """
        Returns the number of items in a list
        """
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        """
        Search an item in the list and returns a boolean value
        In case the item is not where it would be in the list,
        we stpo the search
        """
        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def remove(self, item):
        """
        Remove an item from the list. Assumption is that the
        item is in the list
        """
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous == None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def index(self, item):
        """
        Returns the position of the item in the list if item
        is found. If item is not found returns -1
        """
        current = self.head
        count = 0
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                count += 1
                current = current.get_next()
        if found:
            return count
        return -1

    def insert(self, pos, item):
        """
        Adds a new item to the list at position pos. Assumption is that
        item is not in the list, and there are enough items to have
        position pos
        """
        current = self.head
        previous = None
        count = 0
        found = False

        while current != None and not found:
            if count == pos:
                found = True
            else:
                count += 1
                previous = current
                current = current.get_next()

        temp = Node(item)

        if previous == None:
            # Only one item in the list, perform an add, add
            # to the beginning of the list
            temp.set_next(self.head)
            self.head = temp

        else:
            temp.set_next(previous.get_next())
            previous.set_next(temp)

    def pop(self, pos):
        """
        Removes and returns the item at position pos
        """
        pass
