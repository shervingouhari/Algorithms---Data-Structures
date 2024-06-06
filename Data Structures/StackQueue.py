class StackQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def __str__(self):
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return str(self.stack1)

    def __len__(self):
        return len(self.stack1) + len(self.stack2)

    def reverse(self):
        while self.stack1:
            self.stack2.append(self.stack1.pop())

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            self.reverse()
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            self.reverse()
        return self.stack2[-1]
