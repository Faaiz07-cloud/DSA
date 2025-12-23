"""
2-D Array:
A 2-D array (two-dimensional array) means an array inside another
array — like a table (rows × columns).

You can think of it like an Excel sheet 📊
Each cell has a row and column.

Example (Simple)
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Here:
There are 3 rows
Each row has 3 columns
"""

# 2-D Array Declaration

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(arr)

# Accessing Through Loop
for row in range(len(arr)):
    for column in range(len(arr[row])):
        print(arr[row][column], end=" ")
    print()

# 2-D Array Declaration using random
import random

rows = 5
cols = 5

arr = [[random.randint(1, 100) for j in range(cols)] for i in range(rows)]
print(arr)

for row in range(len(arr)):
    for col in range(len(arr[row])):
        print(arr[row][col], end=" ")
    print()

# 2-D Array Declaration using numpy
import numpy as np

arr = np.random.randint(1,100, size=(6,3))
print(arr)

for row in range(len(arr)):
    for col in range(len(arr[row])):
        print(arr[row][col], end=' ')
    print()

# -------------------------------------------------

# Accessing 2-D Array by index
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print 5
print(arr[1][1])

# print 9
print(arr[2][2])

# Insertion
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Replace 6 with 69 in 2nd row 3rd col
arr[1][2] = 69

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()

# -----------------------------------------------------

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Add a new value 45 after 2 (Don't overwrite) in 1st row

arr[0].insert(2, 45)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()
# -----------------------------------------------

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Add new row [10,11,12] at the end

append = arr.append([10, 11, 12])
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()
# -----------------------------------------------

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# add new row at 1 index

arr.insert(1, [10, 11, 12])
print(arr)

# Deletion

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Delete Whole Array

arr.clear()
print(arr)

# ---------------------------------------------

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Remove 2nd row

arr.pop(1)
# del arr[1]
print(arr)

# ---------------------------------------------

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Remove 5

arr[1].remove(5)
print(arr)

# ---------------------------------------------

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Remove Value of 2nd index at 3rd row (9)

arr[2].pop(2)
print(arr)

# Searching

arr = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

num = int(input("Enter number to search: "))
found = False

for i in range(len(arr)):            # rows
    for j in range(len(arr[i])):     # columns
        if arr[i][j] == num:
            print(f"Found {num} at position ({i}, {j})")
            found = True
            break

if not found:
    print("Not found")


