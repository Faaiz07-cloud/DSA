# Singly Linked List - Search by First Character

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

    def search_by_first_char(self, char):
        if self.head is None:
            print("LinkedList is empty")
            return 0

        result = []
        count = 0
        current = self.head
        while current:
            if current.data[0].lower() == char.lower():
                result.append(current.data)
                count = count + 1
            current = current.next
        if result:
           return f"{count} names found with '{char}': " + ", ".join(result)
        else:
            return f"No names found with '{char}'"

    def search_same_names(self, find_name):
        if self.head is None:
            print("LinkedList is empty")
            return 0

        count = 0
        current = self.head
        while current:
            if current.data == find_name:
                count += 1
            current = current.next
        if count:
           return f"{count} names found with '{find_name}'"
        else:
            return f"No names found with '{find_name}'"

    def print_list(self):
        current = self.head
        while current:
            print(current.data, "->", end=" ")
            current = current.next
        print("None")

ll = LinkedList()
names = [
    "Danish",
    "Dua",
    "Dania",
    "Fatima",
    "Faisal",
    "Hania",
    "Hassan",
    "Hira",
    "Bilal",
    "Bisma",
    "Nimra",
    "Noman",
    "Saad",
    "Saad",
    "Saad",
    "Saad",
    "Sana",
    "Rida",
    "Rayan",
    "Ayesha",
    "Faiz",
    "Farhad"
]
for name in names:
    ll.append(name)
ll.print_list()

print(ll.search_by_first_char("F"))
print(ll.search_by_first_char("D"))

print(ll.search_same_names("Faiz"))

