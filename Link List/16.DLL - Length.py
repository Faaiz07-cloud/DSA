# Doubly Linked List - Length

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

    def length(self):
        if self.head is None:
            print(f"Linked List is empty! Length: 0")
            return None

        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return f"The length of Linked List - {count}"

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
DLL.push_back(50)

print("Traverse Forward")
DLL.traverse_forward()

print("")

print("Traverse Backward")
DLL.traverse_backward()

print("")

print(DLL.length())