# Singly Circular Linked List - Append Back

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    def append_back(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.next = self.head

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = node
        node.next = self.head

    def search(self, value):
        if self.head is None:
            print("Linked list is empty")
            return None

        position = 1
        current = self.head
        while current:
            if current.data == value:
                return f"Node {value} found at position {position}"
            current = current.next
            position += 1
            if current == self.head:
                break
        return f"Node {value} not found"

    def traverse(self):
        if self.head is None:
            print("Linked List is Empty")
            return
        current = self.head
        while current:
            print(current.data, '->', end=" ")
            current = current.next
            if current == self.head:
                break
        print("Back to Head")

ll = SinglyCircularLinkedList()
ll.append_back(10)
ll.append_back(20)
ll.append_back(30)

ll.traverse()

print(ll.search(10))