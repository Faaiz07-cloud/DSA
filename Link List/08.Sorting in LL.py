class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push_back(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def sort(self):
        if self.head is None:
            return

        swapped = True
        while swapped:  # repeat until no swaps
            swapped = False
            current = self.head
            while current.next:
                if current.data > current.next.data:
                    # swap data values
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data,"->", end=" ")
            current = current.next
        print("None")

lst = SinglyLinkedList()
lst.push_back(30)
lst.push_back(20)
lst.push_back(10)
lst.push_back(40)
lst.print_list()
lst.sort()
lst.print_list()