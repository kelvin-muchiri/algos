"""This is a simple implementation of a hash table using separate chaining to resolve
collision resolution. With separate chaining, we create a linked list at each index
of our buckets array containing all keys for a given index

References:
https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd
"""

INITIAL_CAPACITY = 50


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        # the size of our internal array. Note. we set this once for simplicity. In
        # an ideal hash table this should grow and shrink
        self.capacity = INITIAL_CAPACITY
        # no. of elements that have been inserted
        self.size = 0
        # internal array
        self.buckets = [None] * self.capacity

    def hash(self, key):
        """Simple hash function

        Provides a simple degree of uniformity for our purpose
        """
        hashsum = 0
        # For each character in the key

        for idx, c in enumerate(key):
            # Add (index + length of key) ^ (current char code)

            hashsum += (idx + len(key)) ** ord(c)
            # Perform modulus to keep hashsum in range [0, self.capacity - 1]

            hashsum = hashsum % self.capacity
        return hashsum

    def insert(self, key, value):
        """Insert a key value pair into our hashtable"""
        # increment the size of our hash table
        self.size += 1
        # compute the index of key using hash function
        index = self.hash(key)
        # go to the node corresponding to the hash
        node = self.buckets[index]

        if node is None:
            # create a node
            self.buckets[index] = Node(key, value)
            return

        # collision detected
        prev = node

        while node is not None:
            prev = node
            node = node.next

        # add a node at the end of the list with provided key/value
        prev.next = Node(key, value)

    def find(self, key):
        """Find the index and return value of given key"""
        # compute the index of key using hash function
        index = self.hash(key)
        node = self.buckets[index]

        while node is not None and node.key != key:
            node = node.next

        if node is None:
            # Not found
            return None
        else:
            # Found - return the data value
            return node.value

    def remove(self, key):
        """Remove an element from the hash table"""
        # compute the index of key using hash function
        index = self.hash(key)
        node = self.buckets[index]
        prev = None

        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            # 3. Key not found

            return None
        else:
            # 4. The key was found.

            self.size -= 1
            result = node.value
            # Delete this element in linked list

            if prev is None:
                node = None
            else:
                prev.next = prev.next.next
            # Return the deleted value
            return result
