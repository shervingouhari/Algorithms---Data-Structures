from Heap import Heap


class HeapPriorityQueue:
    def __init__(self):
        self.heap = Heap()

    def enqueue(self, item):
        self.heap.insert(item)

    def dequeue(self):
        return self.heap.remove()

    def peek(self):
        return self.heap.array[0]
