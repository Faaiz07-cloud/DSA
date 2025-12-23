# Singly Circular Linked List - Append_Before

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
            return

        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = node
        node.next = self.head

    def append_before(self, target, data):
        if self.head is None:
            print("Circular list is empty.")
            return

        if self.head.data == target:
            node = Node(data)
            last = self.head
            while last.next != self.head:
              last = last.next
            last.next = node
            node.next = self.head
            self.head = node
            return

        current = self.head
        while current.next:
            if current.next.data == target:
                node = Node(data)
                node.next = current.next
                current.next = node
                return
            current = current.next
            if current == self.head:
                break

    def print_list(self):
        current = self.head
        while current:
            print(current.data, '->', end=' ')
            current = current.next
            if current == self.head:
                break
        print("Back to Head")

ll = SinglyCircularLinkedList()
ll.append_back(10)
ll.append_back(20)
ll.append_back(30)
ll.append_back(40)

ll.print_list()

ll.append_before(30, "Ali")
ll.print_list()

ll.append_before(40, "Bob")
ll.print_list()

ll.append_before(10, "Ahmad")
ll.print_list()

ll.append_before("Ahmad", "Bilal")
ll.print_list()






