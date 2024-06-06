class ArrayQueue:
    def __init__(self, length):
        self.length = length
        self.front = 0
        self.rear = 0
        self.size = 0
        self.array = [0] * length

    def __str__(self):
        array = [self.array[(self.front + i) % self.length]
                 for i in range(self.size)]
        return str(array)

    def enqueue(self, item):
        if self.size == self.length:
            raise ValueError("array queue is full")
        self.array[self.rear] = item
        self.rear = (self.rear + 1) % self.length
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise ValueError("array queue is empty")
        item = self.array[self.front]
        self.front = (self.front + 1) % self.length
        self.size -= 1
        return item

    def peek(self):
        if self.size == 0:
            raise ValueError("array queue is empty")
        return self.array[self.front]

    def reverse(self):
        items = [self.dequeue() for i in range(self.size)]
        for item in items[::-1]:
            self.enqueue(item)
