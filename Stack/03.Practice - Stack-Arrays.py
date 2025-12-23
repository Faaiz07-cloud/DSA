# Stack - Arrays

class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        return self.items.append(value)

    def peek(self):
        if len(self.items) == 0:
            print("Stack is Empty!")
            return None
        return self.items[-1]

    def display(self):
        def print_stack(values, i = 0):
            if i == len(values):
                return
            print(values[i], end=" ")
            print_stack(values, i + 1)

        if len(self.items) == 0:
            print("Stack is Empty!")
            return
        print_stack(self.items)

    def pop(self):
        if len(self.items) == 0:
            print("Stack is Empty!")
            return None
        return self.items.pop()

    def is_empty(self):
        if len(self.items) == 0:
            print("Stack is Empty!")
            return
        else:
            print("Stack is not Empty!")

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return self.items

    def search(self, value):
        if len(self.items) == 0:
            print("Stack is Empty!")
            return
        if value in self.items:
            print(f"{value} is found in Stack!")
        else:
            print(f"{value} is not found in Stack!")



stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)

print("Peek Element:",stack.peek())

stack.display()
print("")
print("Pop Element:",stack.pop())
print("Peek Element:",stack.peek())
stack.display()
print("")
stack.is_empty()
print(f"Length of Stack: {stack.size()}")
stack.clear()

# user = int(input("Enter Value:"))
# stack.search(user)







