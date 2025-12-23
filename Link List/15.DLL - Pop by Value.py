# Doubly Linked List - Pop by Value

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

    def pop_by_value(self, target):
        if self.head is None:
            print("Linked List is empty!")
            return
        # agr sirf 1 hi node ho or whi target ho
        if self.head.next is None:
          if self.head.data == target:
            self.head = None
            return
        # agr 1st node hi target ho lekin node multiple hun
        if self.head.data == target:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp
            return

        current = self.head
        while current.next:
            if current.next.data == target:
                temp = current.next
                current.next = current.next.next
                current.next.prev = current
                del temp
                return
            current = current.next
        
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

print(f"Pop by Value\n")

DLL.pop_by_value(30)

print("Traverse Forward")
DLL.traverse_forward()

print("")

print("Traverse Backward")
DLL.traverse_backward()