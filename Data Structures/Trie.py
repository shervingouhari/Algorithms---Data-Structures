class Trie:
    class Node:
        def __init__(self, char, is_word=False):
            self.char = char
            self.is_word = is_word
            self.children = {}

        def __str__(self):
            return str(self.char)

        def __contains__(self, char):
            return self.children.get(char)

    def __init__(self):
        self.root = self.Node(" ")

    def contains(self, word: str):
        node = self.root
        for char in word:
            if not char in node:
                return False
            node = node.children[char]
        return node.is_word

    def insert(self, word: str):
        if " " in word:
            raise ValueError("invalid input")
        node = self.root
        for char in word:
            if not char in node:
                node.children.update({char: self.Node(char)})
            node = node.children[char]
        node.is_word = True

    def remove(self, word: str):
        def _remove(node, index):
            if node == None:
                raise ValueError("node not found")
            if index == len(word):
                node.is_word = False
            else:
                child = node.children.get(word[index])
                _remove(child, index + 1)
                if len(child.children) == 0 and child.is_word == False:
                    node.children.pop(word[index])
        _remove(self.root, 0)

    def traverse_pre_order(self):
        def _traverse_pre_order(node):
            print(node.char)
            for child in node.children.values():
                _traverse_pre_order(child)
        _traverse_pre_order(self.root)

    def traverse_post_order(self):
        def _traverse_post_order(node):
            for child in node.children.values():
                _traverse_post_order(child)
            print(node.char)
        _traverse_post_order(self.root)
