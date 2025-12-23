# TRAVERSAL Questions

# Q1. Print all elements of an array
arr = [10, 20, 30, 40, 50]
for i in arr:
    print(i)
print("-------------------------------------")

# Q2. Print all even numbers from an array
arr = [1, 4, 6, 9, 12, 15]
for i in arr:
    if i % 2 == 0:
        print(i)
print("-------------------------------------")

# Q3. Find the sum of all elements in an array
arr = [5, 10, 15, 20]
total = 0

for i in arr:
    total += i

print(f"Sum of all elements: {total}")

# Another Method
sum(arr)
print(f"Sum of all elements: {sum(arr)}")
print("-------------------------------------")

# Q4. Find the maximum and minimum value (without using max() or min())
arr = [9, 2, 7, 3, 5]
max_value = arr[0]
min_value = arr[0]

# First Method
print(f"Max Element: {max(arr)}")
print(f"Min Element: {min(arr)}")

# Second Method without max() or min()
for i in arr:
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i
print(f"Max Value: {max_value}")
print(f"Min Value: {min_value}")
print("------------------------------------")

# Q5. Count how many numbers are greater than 10
arr = [5, 15, 8, 12, 25, 3]
count = 0

for i in arr:
    if i > 10:
        count += 1
print(f"There are total {count} numbers greater than 10 in this array")
print("------------------------------------")

# INSERTION Questions

# Q1. Insert a number at the end of an array
arr = [1, 2, 3, 4]
append = arr.append(5)
print(arr)
print("------------------------------------")

# Another Method with loop
arr = [1, 2, 3, 4]
num = 5

new_arr = []

for i in arr:
      new_arr += [i]

new_arr.append(num)
print(new_arr)

# for i in range(len(arr)):
#       new_arr += [arr[i]]
#       if len(new_arr) == len(arr):
#           new_arr.append(num)
# print(new_arr)

print("------------------------------------")

# Another Method with loop (Modify Original Array)
arr = [1, 2, 3, 4]
num = 5

for i in range(len(arr) + 1):
    if i == len(arr):
        arr += [num]
        # arr.append(num) # Same as above
print(arr)
print("------------------------------------")

# Q7. Insert a number at a specific position

arr = [10, 20, 40, 50]
# ➤ Insert 30 at index 2

value = arr.insert(2,30)
print(arr)
print("------------------------------------")

# Q8. Insert user input into the array

# arr = [5, 10, 15]
# ➤ Take a number from user and insert at the end
"""
user = int(input("Insert an element in your array: "))
arr.append(user)
print(arr)
print("------------------------------------")
"""

# Q9. Insert an element only if it’s not already present

# arr = [2, 4, 6, 8]
# ➤ If user enters 4, don’t insert (it already exists)
# ➤ If user enters 10, insert it

"""
user = int(input("Insert an element in your array: "))

if user in arr:
    print(f"Element {user} was present in the array.")
else:
    arr.append(user)
    print(arr)
print("------------------------------------")
"""

# Q10. Merge two arrays into one

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
# ➤ Output: [1, 2, 3, 4, 5, 6]

# print(arr1+ arr2)
# arr1.extend(arr2)
# print(arr1)

# arr2.extend(arr1)
# print(arr2)

