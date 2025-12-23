# Doubly Linked List - Searching
from PyInstaller.building.splash_templates import position_window


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push_back(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = node
        node.prev = current

    def searching(self, value):
        if self.head is None:
            print("The list is empty")
            return None

        position = 1
        current = self.head
        while current:
            if current.data == value:
                return f"Node {value} found at position {position}"
            current = current.next
            position += 1
        return "Node not found"

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, "->", end=" ")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.head

        while current and current.next:
              current = current.next

        while current:
            print(current.data, "->", end=" ")
            current = current.prev
        print("None")
DLL = DoublyLinkedList()

DLL.push_back(10)
DLL.push_back(20)
DLL.push_back(30)
DLL.push_back(40)

print("Traverse Forward")
DLL.traverse_forward()

print("")

print("Traverse Backward")
DLL.traverse_backward()

print("")

print(F"Searching\n")

print(DLL.searching(20))

# while True:
#  user_input = int(input("Enter Node to Search: "))
#  print(DLL.searching(user_input))