"""
Operation: Traversal in Array

Traversal means visiting each element of an array one by one — usually
to display, update, or process them.

In simple words:
Traversal = accessing all elements of the array sequentially.

Purpose of Traversal:
   Display array elements
   Search for a specific element
   Perform calculations (like sum, average, max, min)
   Modify elements based on conditions
"""

# Examples

# Traversal of an Array
arr = [1,2,3,4,5,6,7,8,9,10]

"This is Traversal"
for i in arr:
    print(i)
print("")

"Traversal with Index"
for index, i in enumerate(arr):
    print(f"Index: {index} - Value: {i}")
print("")

"Perform Calculations"
arr2 = [33,55,43,76,86,23]

print(f"Sum: {sum(arr2)}")
print(f"Average: {sum(arr2)/len(arr2)}")
print(f"Max: {max(arr2)}")
print(f"Min: {min(arr2)}")