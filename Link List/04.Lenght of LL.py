class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def length(self):
        if self.head is None:
            print("LinkedList is empty")
            return 0
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def print_list(self):
        current = self.head
        while current:
            print(current.data, "→", end=" ")
            current = current.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
ll.print_list()
print("Length of Linked List:",ll.length())