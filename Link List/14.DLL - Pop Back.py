# Doubly Linked List - Pop Back

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

    def pop_back(self):
        if self.head is None:
            print("Linked List is empty!")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None


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

print(f"Pop Last Node\n")

DLL.pop_back()

print("Traverse Forward")
DLL.traverse_forward()

print("")

print("Traverse Backward")
DLL.traverse_backward()