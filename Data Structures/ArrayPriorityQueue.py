class ArrayPriorityQueue:
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(list(reversed(self.array)))

    def enqueue(self, item):
        for i, array_item in enumerate(self.array):
            if item < array_item or item == array_item:
                self.array.insert(i, item)
                return
        self.array.append(item)

    def dequeue(self):
        return self.array.pop()

    def peek(self):
        return self.array[-1]
