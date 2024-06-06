class Stack:
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.array)

    def __len__(self):
        return len(self.array)

    @staticmethod
    def reverse_string(string):
        array = list(string)
        reversed_string = "".join([array.pop() for i in range(len(array))])
        return reversed_string, string[::-1]

    @staticmethod
    def reverse_array(array):
        stack = Stack()
        for i in range(len(array)):
            stack.push(array.pop())
        return stack

    @staticmethod
    def is_balanced_expression(string):
        open_symbols = ["[", "{", "(", "<"]
        close_symbols = ["]", "}", ")", ">"]
        symbol_mapping = {c: o for o, c in zip(open_symbols, close_symbols)}
        stack = Stack()
        for char in string:
            if char in open_symbols:
                stack.push(char)
            elif char in close_symbols:
                if not stack:
                    return False
                if stack.peek() == symbol_mapping[char]:
                    stack.pop()
                else:
                    return False
        return not stack

    def push(self, item):
        self.array.append(item)

    def pop(self):
        return self.array.pop()

    def peek(self):
        return self.array[-1]
