from utils import indexify


class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.previous = None
            self.next = None

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __str__(self):
        return str([node.value for node in self])

    def __getitem__(self, index):
        if index < 0:
            index = self.size - abs(index)
        if index > self.size - 1 or index < 0:
            raise IndexError("index out of range")
        if (self.size - 1 - index) < index:
            curr = self.tail
            for i in range(self.size - 1 - index):
                curr = curr.previous
            return curr
        for i, node in enumerate(self):
            if i == index:
                return node

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def index(self, value):
        for i, node in enumerate(self):
            if node.value == value:
                return i
        raise ValueError("value not found")

    def contains(self, value):
        try:
            self.index(value)
            return True
        except ValueError:
            return False

    def reverse(self):
        if not self.size == 0:
            first = self.head
            second = first.next
            while True:
                first.next, first.previous = first.previous, first.next
                if second is None:
                    break
                first, second = second, second.next
            self.head, self.tail = self.tail, self.head

    def appendleft(self, value):
        new_node = self.Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.size += 1

    def append(self, value):
        new_node = self.Node(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, index, value):
        index = indexify(self.size, index)
        if index == 0:
            self.appendleft(value)
        elif index == self.size:
            self.append(value)
        else:
            first = self[index - 1]
            second = self.Node(value)
            third = first.next
            first.next, second.next = second, third
            third.previous, second.previous = second, first
            self.size += 1

    def popleft(self):
        if self.size == 0:
            raise ValueError("linked list is empty")
        node = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            new_first = self.head.next
            new_first.previous = None
            self.head = new_first
        self.size -= 1
        return node

    def pop(self):
        if self.size == 0:
            raise ValueError("linked list is empty")
        node = self.tail
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            penultimate = self.tail.previous
            penultimate.next = None
            self.tail = penultimate
        self.size -= 1
        return node

    def remove(self, value):
        if self.size == 0:
            raise ValueError("linked list is empty")

        def _find():
            for node in self:
                if node.value == value:
                    return node
            raise ValueError("node not found")
        second = _find()
        if self.head == second and self.tail == second:
            self.head = None
            self.tail = None
        else:
            first = second.previous
            third = second.next
            if first is None:
                self.popleft()
                return
            if third is None:
                self.pop()
                return
            first.next, third.previous = third, first
            self.size -= 1
