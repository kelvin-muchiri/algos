"""
Search
    - Prefix - If there is at least 1 word with a given prefix or not
    - Whole word - If the whole word exists in a trie or not
Delete
    - Whole word
    - All words that start with a given prefix


Time complexity:
    Insertion: O(l x n) where l is the length of a word, n is the number of
    words to be inserted

    Search: O(l) where l is the length of the word

References:
https://www.youtube.com/watch?v=AXjmTQ8LEoI&ab_channel=TusharRoy-CodingMadeSimple
"""
from typing import Dict


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self) -> None:
        self.root: 'TrieNode' = TrieNode()

    def insert_iterative(self, word: str) -> None:
        """Iterative insert"""
        current = self.root

        for i in range(len(word)):
            ch = word[i]
            node = current.children.get(ch, None)

            if not node:
                node = TrieNode()
                current.children[ch] = node

            current = node

        # mark the end of word as true
        current.is_end_of_word = True

    def insert_recursive(self, word: str) -> None:
        """Recursive insert"""
        self._insert_recursive_util(self.root, word, 0)

    def _insert_recursive_util(self, current_node: 'TrieNode', word: str, index: int) -> None:
        if index == len(word):
            current_node.is_end_of_word = True
            return

        char = word[index]
        node = current_node.children.get(char, None)

        if not node:
            node = TrieNode()
            current_node[char] = node

        self._insert_recursive_util(node, word, index + 1)

    def search_iterative(self, word: str) -> bool:
        """Iterative search"""
        current = self.root

        for i in range(len(word)):
            ch = word[i]
            node = current.children.get(ch, None)

            if not node:
                return False

            current = node

        return current.is_end_of_word

    def search_recursive(self, word: str) -> bool:
        """Recursive search"""
        return self._search_recursive_util(self.root, word, 0)

    def _search_recursive_util(self, current_node: 'TrieNode', word: str, index: int) -> bool:
        if index == len(word):
            return current_node.is_end_of_word

        char = word[index]
        node = current_node.children.get(char, None)

        if not node:
            return False

        self._insert_recursive_util(node, word, index + 1)

    def delete(self, word):
        self._delete_util(self.root, word, 0)

    def _delete_util(self, current_node: 'TrieNode', word: str, index: int) -> bool:
        if index == len(word):
            # end of word is reached
            if not current_node.is_end_of_word:
                # word does not exist in the trie
                return False

            current_node.is_end_of_word = False
            # if current has no other mapping return true
            # so that the parent can delete reference to node if mapping is is empty
            return len(current_node) == 0

        ch = word[index]
        node = current_node.children.get(ch, None)

        if not node:
            # word does not exist in the trie
            return False

        should_delete_current_node = self._delete_util(node, word, index + 1)

        if should_delete_current_node:
            del current_node.children[ch]
            # return true if no mappings are left
            return len(current_node) == 0

        return False
