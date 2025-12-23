# Doubly Linked List - Insert Before

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

    def insert_before(self, target, data):
        if self.head is None:
            print("DoublyLinkedList is empty!")
            return

        current = self.head

        while current.next:
            if current.next.data == target:
                node = Node(data)
                node.next = current.next
                node.prev = current
                current.next = node
                if node.next:
                    node.next.prev = node
                return
            current = current.next
        print(f"NodE {target} not found!")


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

DLL.push_back(25)
DLL.push_back(35)
DLL.push_back(55)
DLL.push_back(65)

print("Traverse Forward")
DLL.traverse_forward()

print("")

print("Traverse Backward")
DLL.traverse_backward()

print("")

print(f"Insert 45 before 55\n")

DLL.insert_before(55, 45)

print("Traverse Forward")
DLL.traverse_forward()

print("")

print("Traverse Backward")
DLL.traverse_backward()
