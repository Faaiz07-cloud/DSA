"""
Array Operation: Deletion

Deletion means removing an element from the array — either by its value or index.
After deletion, the remaining elements shift left to fill the gap.

Types of Deletion

By Value	                      arr.remove(30)
By Index	                      arr.pop(2)
Last Element	                  arr.pop()
Entire Array	                  arr.clear()
Using del keyword	              del arr[1]
"""

# Example
arr = [1,2,3,4,5,6,7,8,9]
print(arr)

"By Value"
arr.remove(5)
print(arr)

"By Index"
arr.pop(6)
print(arr)

"Last Element"
arr.pop()
print(arr)

"Using del keyword"
del arr[2]
print(arr)

"Entire Array"
arr.clear()
print(arr)


