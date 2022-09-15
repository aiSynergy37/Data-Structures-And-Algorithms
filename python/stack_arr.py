from sys import maxsize

class Stack:
    # Function to build the DS
    # It initializes the size of stack to zero
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if (self.isEmpty()):
            return str(-maxsize - 1)
        return self.stack.pop()

    def peek(self):
        if (self.isEmpty()):
            return str(-maxsize - 1)
        return self.stack.pop()

    def size(self):
        return len(self.stack)
