# Singly Circular Linked List - Append After

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyCircularLinkedList:
    def __init__(self):
        self.head = None

    def append_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def append_after(self, target, data):
        current = self.head
        while current:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            if current == self.head: # When one iteration completes
                break
        print(f"Node {target} not found.")

    def traverse(self):
        current = self.head
        while current:
             print(current.data, "->", end=" ")
             current = current.next
             if current == self.head:
                 break
        print("Back to Head")

ll = SinglyCircularLinkedList()
ll.append_back(10)

ll.append_after(10,50)
ll.append_after(10,70)
ll.append_after(10,90)
ll.append_after(70,30)
ll.append_after(50,300)


ll.traverse()