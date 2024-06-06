from utils import indexify


class Array:
    def __init__(self, _type, length, _list, dynamic=False):
        self.type = _type
        self.length = length
        self.dynamic = dynamic
        self.size = 0
        self.array = [None] * length

        if not isinstance(_list, list):
            raise TypeError("only objects of type list are accepted")
        if len(_list) > length:
            raise ValueError("list is larger than length")
        for item in _list:
            if not isinstance(item, self.type):
                raise TypeError("array items must be of the same type")
        for index, item in enumerate(_list):
            self[index] = item

    def __str__(self):
        return str(self.array)

    def __getitem__(self, index):
        return self.array[index]

    def __setitem__(self, index, item):
        if item != None and not isinstance(item, self.type):
            raise TypeError("array items must be of the same type")
        self.array[index] = item

    def resize(self):
        if self.dynamic:
            self.array += [None] * self.length
            self.length *= 2
        else:
            raise OverflowError("array is full")

    def index(self, item):
        for i in range(self.length):
            if self[i] == item:
                return i
        raise ValueError("item not found")

    def insert(self, index, item):
        if not isinstance(item, self.type):
            raise TypeError("array items must be of the same type")
        index = indexify(self.length, index)
        if index == self.length:
            self.resize()
        for i in range(index, self.size, -1):
            self[i + 1] = self[i]
        self[index] = item
        self.size += 1

    def remove(self, item):
        if self.size == 0:
            raise ValueError("array is empty")
        index = self.index(item)
        for i in range(index, self.length - 1):
            self[i] = self[i + 1]
        self[-1] = None
        self.size -= 1

    def reverse(self):
        start = 0
        end = self.length - 1
        while start != end and start < self.length - 1 and end > 0:
            self[end], self[start] = self[start], self[end]
            start += 1
            end -= 1
