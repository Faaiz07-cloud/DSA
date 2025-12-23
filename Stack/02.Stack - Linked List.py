# Stack - Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackList:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.count += 1

    def peek(self):
        if self.top is None:
            print("Stack is empty")
            return None
        return self.top.data

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        current = self.top
        while current:
            print(current.data,'->', end=" ")
            current = current.next
        print("None")

    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None
        popped = self.top.data
        self.top = self.top.next
        self.count -= 1
        return popped

    def is_empty(self):
        if self.top is None:
            print("Stack is empty")
            return

    def clear(self):
        self.top = None
        self.count = 0

    def size(self):
        if self.top is None:
            print("Stack is empty")
            return None
        return f"Size of Stack: {self.count}"

    def search(self, value):
        if self.top is None:
            print("Stack is empty")
            return None
        position = 1
        current = self.top
        while current:
            if current.data == value:
                return f"Node {value} found at position {position}"
            position += 1
            current = current.next
        return f"Node {value} not found"

    def size_2(self):
        if self.top is None:
            print("Stack is empty")
            return None
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return f"Size of Stack: {count}"

    def display_2(self): # using recursion
        def reverse_print(node):
            if node is None:
                return
            reverse_print(node.next)
            print(node.data,'->', end=" ")
        if self.top is None:
            print("Stack is empty")
            return
        reverse_print(self.top)
        print("None")

    def display_3(self):
        if self.top is None:
            print("Stack is empty")
            return
        values = []
        current = self.top
        while current:
            values.append(current.data)
            current = current.next
        print(" -> ".join(map(str, reversed(values))), "-> None")
stack = StackList()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

stack.display()
print("")

print("Top Element:",stack.peek())

print("")

print("Popped Element:",stack.pop())

print("")

stack.display()

print("")

print("Top Element:",stack.peek())

# stack.is_empty()

print("")

print(stack.size())

# stack.clear()

# stack.display()

print(stack.search(4))

print(stack.size_2())

stack.display_2()

stack.display_3()

