"""
Operation: Insertion in Array
Insertion means adding a new element to the array at a specific
position (beginning, middle, or end).

When we insert, the new element takes a position, and existing
elements shift to make space.

Types of Insertions:
                     At the end     	append()
                     At the beginning	insert(0, 5)
                     In the middle	    insert(2, 25)
"""
from platformdirs import user_log_dir

#Example

"Simple Insertion"
arr = [1,2,3,4,5]

"At the end - Insertion"
arr.append(6)
print(arr)

"In the beginning - Insertion"
arr.insert(0, 0)
print(arr)

"In the middle - Insertion"
arr.insert(3, 77)
print(arr)

"Update Array"
arr[7] = 543234
print(arr)

# Insertion Using User Input (append)
# arr2 =[]
# while True:
#       user = int(input("Insert an element in your array: "))
#       arr2.append(user)
#       print(arr2)

# Insertion Using User Input (insert)
# arr3 =[33,43,54,43]
# while True:
#       user = int(input("Insert an element in your array: "))
#       arr3.insert(2, user)
#       print(arr3)

# Update Array Using User Input
arr4 =[33,43,54,43]
while True:
      user = int(input("Insert an element in your array: "))
      arr4[2] = user
      print(arr4)
