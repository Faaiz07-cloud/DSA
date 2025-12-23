class Node:
    def __init__(self,data):
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

    def search(self,value):
      if self.head is None:
          print("Linked List is empty")
          return 0

      position = 1
      current = self.head

      while current:
          if current.data == value:
              return f"Value {value} Found at position {position}"
          current = current.next
          position += 1
      return f"Value {value} Not Found"

    def print_list(self):
        current = self.head
        while current:
            print(current.data,"->", end=" ")
            current = current.next
        print("None")

ll = LinkedList()
data = [1,2,3,4,5]
for i in data:
 ll.append(i)
ll.print_list()
print(ll.search(2))