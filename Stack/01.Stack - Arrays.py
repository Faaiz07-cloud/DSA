"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle — the element
inserted last is removed first.

Core operations:
push(item) — place item on top
pop() — remove and return the top item
peek() or top() — return the top item without removing
is_empty() — true if stack has no items
size() — number of items

Time complexity:
push, pop, peek, is_empty, size → O(1)
"""

# Stack - Arrays

class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
       self.data.append(item)

    def pop(self):
        if len(self.data) == 0:
            print("Stack is empty")
            return None
        return self.data.pop()

    def peek(self):
        if len(self.data) == 0:
            print("Stack is empty")
            return None
        return self.data[-1]

    def is_empty(self):
        if len(self.data) == 0:
            print("Stack is empty")

    def size(self):
        return len(self.data)

    def search(self, item):
        if len(self.data) == 0:
            print("Stack is empty")
            return None
        if item in self.data:
            return f"Node {item} found in stack"
        else:
            return f"Node {item} not found in stack"

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print(stack.pop())

# print(stack.peek())

# stack.is_empty()

print(stack.size())

stack.push(5)

print(stack.peek())

print(stack.size())

print(stack.search(55))































# class StackList:
#     def __init__(self):
#         self._data = []
#
#     def push(self, item):
#         self._data.append(item)
#
#     def pop(self):
#         if not self._data:
#             raise IndexError("pop from empty stack")
#         return self._data.pop()
#
#     def peek(self):
#         if not self._data:
#             raise IndexError("peek from empty stack")
#         return self._data[-1]
#
#     def is_empty(self):
#         return len(self._data) == 0
#
#     def size(self):
#         return len(self._data)
#
#     def __repr__(self):
#         return f"StackList({self._data})"
#
# s = StackList()
# s.push(10)
# s.push(20)
# # print(s.peek())   # 20
# print(s.pop())    # 20
# print(s.pop())    # 10
# print(s.pop())  # would raise IndexError
