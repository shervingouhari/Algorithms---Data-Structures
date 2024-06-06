from collections import deque
from utils import hash1


class HashTable:
    class Entry:
        def __init__(self, key, value):
            self.key = key
            self.value = value

        def __repr__(self):
            return str(f"{{{self.key}: {self.value}}}")

    def __init__(self, length):
        self.length = length
        self.table = [deque() for i in range(length)]

    def __str__(self):
        return str([str(i) for i in self.table])

    def update(self, kwarg):
        for key, value in kwarg.items():
            linked_list = self.table[hash1(key, self.length)]
            for node in linked_list:
                if node.key == key:
                    node.value = value
                    return
            linked_list.append(self.Entry(key, value))

    def remove(self, key):
        linked_list = self.table[hash1(key, self.length)]
        for node in linked_list:
            if node.key == key:
                linked_list.remove(node)
                return
        raise KeyError("entry not found")

    def get(self, key, default=None):
        linked_list = self.table[hash1(key, self.length)]
        for node in linked_list:
            if node.key == key:
                return node.value
        return default
