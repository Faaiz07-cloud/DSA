# Stack - Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0 # Optional for Size

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.count += 1

    def display_1(self):
        if self.top is None:
            print("Stack is Empty!")
            return

        current = self.top
        while current:
            print(current.data, '->', end=" ")
            current = current.next
        print("None")

    def display_2(self):
        if self.top is None:
            print("Stack is Empty!")
            return
        values = []
        current = self.top
        while current:
            values.append(current.data)
            current = current.next
        print(" -> ".join(map(str, values)), "-> None")
        # For Reverse Print
        # print(" -> ".join(map(str, reversed(values))), "-> None")

    def display_3(self):
        def print_stack(node):
            if node is None:
                return
            # print(node.data, "->", end=" ")
            print_stack(node.next)
            # Function Calls after Return (Reversed)
            print(node.data, "->", end=" ")

        if self.top is None:
            print("Stack is Empty!")
            return
        print_stack(self.top)
        print("None")

    def peek(self):
        if self.top is None:
            print("Stack is Empty!")
            return None
        return  self.top.data

    def pop(self):
        if self.top is None:
            print("Stack is Empty!")
            return None
            return None
        popped = self.top.data
        self.top = self.top.next
        self.count -= 1
        return popped

    def size_1(self):
        if self.top is None:
            print("Stack is Empty!")
            return None
        count = 0
        current = self.top
        while current:
            count += 1
            current = current.next
        return f"Size of Stack is: {count}"

    def size_2(self):
        return f"Size of Stack is: {self.count}"

    def clear(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        if self.top is None:
            print("Stack is Empty!")
            return True
        else:
            print("Stack is not Empty!")
            return False

    def search(self, value):
        if self.top is None:
            print("Stack is Empty!")
            return None
        position = 1
        current = self.top
        while current:
            if current.data == value:
                return f"Node {value} at position {position}"
            current = current.next
            position += 1
        return f"Node {value} not Found!"

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)

stack.display_1()
# stack.display_2()
# stack.display_3()

# print(stack.size_1())
print(stack.size_2())

print("Peek Element -",stack.peek())
print("Pop Element -",stack.pop())
print("")
print("Peek Element -",stack.peek())
stack.display_1()

# print(stack.size_1())
print(stack.size_2())

# stack.clear()

print(stack.is_empty())

print(stack.search(20))

