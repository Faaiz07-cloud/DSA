# Create a 3×3 2D array and print all elements in matrix form.

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Answer No. 1")
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()

print()

# Print only the first row of the given array.

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Answer No. 2")

print(arr[0])

for i in arr[0]:
    print(i, end=" ")
    print()

print()

# Print only the last column of the given array.

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Answer No. 3")

print(arr[2])

for i in arr[2]:
    print(i, end=" ")
    print()

print()

# Find and print the sum of all elements in a 2D array.

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Answer No. 3")
total = 0

for row in arr:
    for col in row:
        total += col

print("The sum of 2-D Array:",total)

print()

# Count how many elements are greater than 50 in a 5×5 random 2D array.

arr = [
    [12, 25, 37, 48, 59],
    [60, 15, 72, 33, 95],
    [41, 52, 63, 74, 85],
    [96, 27, 18, 69, 78],
    [81, 92, 53, 44, 67]
]
print("Answer No. 4")

count = 0

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] > 50:
            count += 1

print("Numbers greater than 50:", count)

print()

# Replace all elements less than 10 with 0.

arr = [
    [3, 7, 2, 15, 9],
    [5, 8, 12, 6, 10],
    [1, 9, 4, 18, 7],
    [2, 14, 5, 3, 11],
    [6, 8, 20, 9, 4]
]

print("Answer No. 5")

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < 10:
            arr[i][j] = 0
        print(arr[i][j], end=" ")
    print()

print()

# Create a 5×5 2D array using loops, random (1,100)
import random

rows = 5
cols = 5

print("Answer No. 6")
arr = [[random.randint(1, 100) for j in range(cols)] for i in range(rows)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()

print()

# Create a 5×5 2D array using loops, random (1,100), numpy

import numpy as np

print("Answer No. 7")
arr = np.random.randint(1, 100, size=(5, 5))

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()

print()

# Insert a new row [11, 12, 13] at index 1.

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Answer No. 8")

new_row = arr.insert(1, [11, 12, 13])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()

print()

# Delete the last row of the array.

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Answer No. 9")

del_row = arr.pop()

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()

print()

# Delete the first column of the array (using loop).

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Answer No. 9")

for i in range(len(arr)):
    del arr[i][0]

# for i in range(len(arr)):
#     arr[i].pop(2)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()

print()

# Search for a number entered by the user and print its position.

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Answer No. 10")

found = False
user = int(input("Enter number to search: "))

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == user:
            print(f"The number present at position ({i}, {j})")
            found = True

if not found:
    print(f"The number is not present in array")


# Find the maximum and minimum element in a 2D array.

arr = [
    [9, 2, 7, 3, 5],
    [5, 2, 1, 6, 0],
    [5, 2, 7, 3, 9],
    [1, 2, 1, 3, 5],
    [0, 7, 9, 3, 1],
]
max_value = arr[0][0]
min_value = arr[0][0]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] > max_value:
            max_value = arr[i][j]
        if arr[i][j] < min_value:
            min_value = arr[i][j]

print(max_value)
print(min_value)

# Calculate the sum of each row separately and print the results.

arr = [
    [12, 25, 37, 48, 59],
    [60, 15, 72, 33, 95],
    [41, 52, 63, 74, 85],
    [96, 27, 18, 69, 78],
    [81, 92, 53, 44, 67]
]

# for i in range(len(arr)):
#     print(f"The sum of Row {i+1}",sum(arr[i]))


for i in range(len(arr)):
    total = 0
    for j in range(len(arr[i])):
        total += arr[i][j]
    print(f"Sum of Row {i + 1}: {total}")

# Calculate the sum of each column separately.

arr = [
    [12, 25, 37, 48, 59],
    [60, 15, 72, 33, 95],
    [41, 52, 63, 74, 85],
    [96, 27, 18, 69, 78],
    [81, 92, 53, 44, 67]
]

for j in range(len(arr[0])):
     total = 0
     for i in range(len(arr)):
         total += arr[i][j]
     print(f"Sum of Column {j + 1}: {total}")

# Create a 4×4 random array and print only the diagonal elements.
import random

arr = [[random.randint(1,100) for x in range(5)] for y in range(5)]

for i in arr:
    print(i)

# Diagonal Numbers

for i in range(len(arr)):
    print("  "*i,arr[i][i])

# Swap the first row with the last row in a 2D array.
# Swap the first column with the last column in a 2D array.


arr = [
    [12, 25, 37, 48],
    [60, 15, 72, 33],
    [41, 52, 63, 74],
    [96, 27, 18, 69]
]

arr[0], arr[3] = arr[3], arr[0]
print(arr)

arr = [
    [12, 25, 37, 48],
    [60, 15, 72, 33],
    [41, 52, 63, 74],
    [96, 27, 18, 69]
]

for i in range(len(arr)):
    arr[i][0], arr[i][-1] = arr[i][-1], arr[i][0]
    print(arr[i])



