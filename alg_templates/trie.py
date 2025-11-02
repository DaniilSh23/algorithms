"""
Trie (Префиксное дерево)
Условия: "Поиск по префиксу", "автодополнение"
Задачи LeetCode: #208 (Implement Trie), #212 (Word Search II)
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True