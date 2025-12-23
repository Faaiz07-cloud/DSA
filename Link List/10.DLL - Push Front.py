# Doubly Linked List - Push Front

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push_front(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        node.next = self.head
        self.head.prev = node
        self.head = node

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

DLL.push_front(10)
DLL.push_front(20)
DLL.push_front(30)
DLL.push_front(40)

print("Traverse Forward")
DLL.traverse_forward()

print("")

print("Traverse Backward")
DLL.traverse_backward()
