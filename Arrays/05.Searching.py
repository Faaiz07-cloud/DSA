"""
Array Operation: Searching

Searching means finding the position (index) or existence
of a specific element in an array.

Types of Searching

Linear Search	             Checks each element one by one
	        Small / unsorted arrays

Binary Search	    Repeatedly divides the array to find element
	       Sorted arrays only
"""

# Example

# Simple Searching

arr = [1,2,3,4,5]
if 2 in arr:
    print("2 is present")
    # print(f"2 is present at {arr.index(2)}") # with index
else:
    print("2 is not present")

# Another Basic Searching
# We use it when the array size is small, and we know the value is present.
arr2 = [1,2,3,4,5,6,7]
value = 6
if value in arr2:
    print("Value is present", arr2.index(value))
else:
    print("Value is not present")

"""
If the array is small or not sorted, and you don’t know whether
the value exists — then you use Linear Search with a simple loop
(checking each element one by one).
"""
arr = [i for i in range(1, 51)]
print(arr)
x = 45

found = False
for i in range(len(arr)):
    if arr[i] == x:
        print(f"Element {x} is present at index {i}")
        found = True
        break

if not found:
    print(f"Element {x} is not present!")

import random
array = [random.randint(1, 100) for i in range(1, 71)]
x = 77
found = False

for i in range(len(array)):
    if array[i] == x:
        print(f"Element {x} found at index {i}")
        found = True
        break
if not found:
    print(f"Element {x} is not present")
