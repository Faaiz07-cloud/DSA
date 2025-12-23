"""
A Circular Linked List is just like a normal
Singly Linked List or Doubly Linked List, except
the last node’s next pointer points back to the
first node instead of being None.

So, the list forms a circle
          (no node has next = None).


1. Singly Circular Linked List
    10->20->30->40->50->(Back to Head)
    10.next = 20
    20.next = 30
    30.next = 40
    40.next = 50
    50.next = 10

2. Doubly Circular Linked List
   10<->20<->30<->40<->50<->(Back to Head)
   10.next = 20
   20.prev = 10
   20.next = 30
   30.prev = 20
   30.next = 40
   40.prev = 30
   40.next = 50
   50.prev = 40
   50.next = 10
   10.prev = 50
"""