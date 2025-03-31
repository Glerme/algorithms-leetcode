class Stack:
    def __init__(self, max_length=1000):
        self.items = [] * max_length
        self.max_length = max_length
        self.pointer = 0

    def push(self, item):
        self.items[self.pointer] = item
        self.pointer += 1

    def pop(self):
        if not len(self.items):
            raise IndexError("Empty List")

        return self.items.pop()

    def peek(self):
        if not len(self.items):
            raise IndexError("Empty List")

        return self.items[-1]

    def size(self):
        return self.pointer
