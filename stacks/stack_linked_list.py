class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.top is None:
            raise IndexError("Empty stack")

        popped_node = self.top
        self.top = popped_node.next
        self._size -= 1

        return popped_node.value

    def peek(self):
        if self.top is None:
            raise IndexError("Empty stack")

        return self.top.value

    def size(self):
        return self._size


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())        # Output: 3
print(stack.peek())       # Output: 2
print(stack.size())       # Output: 2
