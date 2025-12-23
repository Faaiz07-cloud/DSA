"""
Array:
     An Array is a collection of similar data items stored in one
     variable — instead of using many variables.

In Simple Words:
                 Array is like a box with many small compartments, where each
                 compartment holds one value.

Why We Use Arrays:
                  ✅ To store many values together
                  ✅ To access data easily using index
                  ✅ To loop through values easily
                  ✅ Saves memory and makes code clean

Types of Array:
               1-D Array
               2-D Array
               Multi-D Array
               Dynamic Arrays (Lists in Python)
"""

# Basic Functions of Array

# Array Declaration
arr = [1,2,3,4,5,6,6]

print(f"Whole Array: {arr}") # Whole Array
print(f"Length of an array: {len(arr)}") # Length of Array
print(f"Value of 2nd Index: {arr[2]}") # Value of 2nd Index
print(f"Max Value of Array: {max(arr)}") # Max number in an array
print(f"Min Value of Array: {min(arr)}") # Min number in an array
print(f"Count of 6: {arr.count(6)}") # Counts how many 6s are in array
print("Printing array through Loop")
for i in arr:
    print(i)
print("")

arr.reverse() # Reversing an array
print(f"Reversed Array: {arr}\n")

# Array Declaration using Input
# arr2 = []
# while True:
#   user = int(input("Enter Element: "))
#   arr2.append(user)
#   for i in arr2:
#       print(i)
#   print("")
#   print(arr2)

# Array Declaration using Loop
arr2 = [i for i in range(1,80)]
print(f"{arr2}\n")


# Array with different Data-Type
arr3 = ["Umar", "Ali", "Ahmad", 7, 9, 8]
print(f"Mix Data-Type Array: {arr3}")
print(arr3[1])

arr4 = [1, 2, 3]
append = arr4.append(4) # Value appended at the end of Array
print(f"Appended Array: {arr4}")

insert = arr4.insert(2, 5) # Inserts value 5 at index 2; shifts existing elements to the right
print(f"Inserted Array: {arr4}")

sort = arr4.sort()
print(f"Sorted Array: {arr4}")

pop = arr4.pop() # Pop out value of last index if none index is provided
print(f"Popped Array: {arr4}")

pop2 = arr4.pop(2) # Pop out value of 2nd index
print(f"Popped Array: {arr4}")

remove = arr4.remove(4) # Remove Value 4
print(f"Remove Array: {arr4}")

'''
Pop : Pop Value by Index
Remove: Remove Value by Value
'''

# Updating an array
arr5 = [1,2,3,4,5,6,7,8,9]
arr5[5] = 56 # Value of 5th Index becomes 56
print(arr5)

# Searching in an array
if 5 in arr5:
    print("5 is in arr5\n")
else:
    print("5 is not in arr5\n")

"Merging"
arr6 = [1,2,3,4,5,6,7,8,9]
arr7 = [10,11,12,13,14,15,16,17,18,19,20]

# print(arr6+arr7) # Merging Arrays
# arr6.extend(arr7) # Another Method
# print(arr6)
# arr7.extend(arr6)
# print(arr7)