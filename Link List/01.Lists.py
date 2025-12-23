"""
A list is an ordered collection of elements (items).

That means:
Each element has a specific position (called an index).
You can access, insert, remove, or update elements using their index.
Lists can hold duplicate values (e.g., [2, 2, 5] is valid).
The order of insertion is maintained.

Major Implementations of Lists:
1. Arrays
2. Link Lists
3. Stack
4. Queue etc
"""

"""
Linked List

A Linked List is a linear data structure where data is stored in separate
nodes, and each node is connected to the next one using a pointer (reference).

Each node has two parts:
Data → stores the actual value.
Next → stores the address (reference) of the next node.

Types:

Singly Linked List → points only to the next node.
Doubly Linked List → points to next and previous nodes.
Circular Linked List → last node connects back to the first.

Why use linked lists? (advantages)

Dynamic size (grow/shrink at runtime).
Insert/delete at head (or given node) O(1) — no shifting like arrays.
Useful jab frequent insert/delete ho (especially at front).

Disadvantages

Random access (x).
Extra memory for pointers.
Cache-unfriendly (non-contiguous memory).

Basic operations

Traverse / iterate: O(n)
Insert at head: O(1)
Insert at tail: O(n) (unless tail pointer maintain karo -> O(1))
Insert at specific: O(n)
Delete by value: O(n)
Search: O(n)
"""

# Basic Program of Linked List (Manually Node Creation & Connections)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Passing Data
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

# Making Connections
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

# Making Head Node
Head = n1

# Traversing with Function

def print_list(head):
    current = head  # Start Traversing from First Node
    while current:
        print(current.data, end=' ')
        current = current.next
    # print("None") # Optional

print_list(Head)




