# Singly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data): # Insert at End / Push Back
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_start(self, data): # Insert at Start / Push Front
       new_node = Node(data)
       if self.head is None:
            self.head = new_node
            return
       new_node.next = self.head
       self.head = new_node

    def insert_after(self, target, data): # Insert after Node
        if self.head is None:
            print("Linked List is empty!")
            return
        current = self.head
        while current:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print(f"Node with data {target} not found.")

    def insert_before(self, target, data): # Insert before Node
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data == target:
             self.insert_at_start(data)
             return

        current = self.head
        while current.next:
            if current.next.data == target:
               new_node = Node(data)
               new_node.next = current.next
               current.next = new_node
               return
            current = current.next
        print(f"Node with data {target} not found.")

    def delete_start(self): # Delete first Node / Pop Front
        if self.head is None:
            print("Linked List is empty!")
            return
        temp = self.head
        self.head = self.head.next
        del temp

    def delete_end(self): # Delete Last Node / Pop Back
        if self.head is None:
            print("Linked List is empty!")
            return

        # if only one node
        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_by_value(self, value):
        if self.head is None:
            print("Linked List is empty!")
            return

        # if value at first node
        if self.head.data == value:
            self.delete_start()
            return

        current = self.head
        while current.next:
            if current.next.data == value:
                temp = current.next
                current.next = current.next.next
                del temp
                return
            current = current.next
        print(f"Node with data {value} not found.")

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end = " ")
            current = current.next

ll = SinglyLinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.insert_at_end(50)
ll.insert_at_start("Hello")
ll.insert_at_start("Thanks")
ll.insert_after(30, "Umar")
ll.insert_after(50, "Umair")
ll.insert_after(10, "Faiz")
ll.insert_before(20, "Zeeshan")
ll.insert_before("Thanks", "Ali")
ll.delete_start()
ll.delete_end()
ll.delete_by_value(40)

ll.print_list()



