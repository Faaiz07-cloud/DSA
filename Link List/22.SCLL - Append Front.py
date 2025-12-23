# Singly Circular Linked List - Append Front

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    def append_front(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.head.next= self.head
            return
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = node
        node.next = self.head
        self.head = node

    def traverse(self):
     current = self.head
     while current:
            print(current.data, '->', end=' ')
            current = current.next
            if current == self.head:
                break
     print("Back to Head")

ll = SinglyCircularLinkedList()
ll.append_front(1)
ll.append_front(2)
ll.append_front(3)


ll.traverse()