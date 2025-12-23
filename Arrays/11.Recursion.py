# ----- Basic Recursion Programs -----

# def open_box(n):
#     # Base Case (Where function terminates)
#     if n == 1:
#         print(f"Opening Box {n}")
#         print("Smallest Box found")
#         print(f"Closing Box {n}")
#         return
#     # Recursive Case
#     print(f"Opening Box {n}")
#     open_box(n - 1)
#     # Back Tracking
#     print(f"Closing Box {n}")
# open_box(5)

"""
When the function is first called with n = 5, the
condition n == 1 is false, so it prints “Opening Box 5”
and then calls itself recursively with n - 1,
which means the next function call receives n = 4.

The same process continues:

For n = 4, the condition is false, so it prints
“Opening Box 4” and calls open_box(3).

For n = 3, it prints “Opening Box 3” and 
calls open_box(2).

For n = 2, it prints “Opening Box 2” and calls
open_box(1).

Finally, when n becomes 1, the condition n == 1
becomes true,
so the base case is reached.
At this point, the function prints “Opening Box 1”
and “Smallest Box found!”,
then it returns, meaning recursion stops here.

After the base case was reached (when n == 1),
the function began backtracking — that means once
the base case returned, the function started going
back step by step, executing all the previous calls
for n = 2, 3, 4, and 5 in reverse order. In simple
words, it returned back through all the earlier
function calls one by one.
"""

# def print_numbers(n):
#     if n == 1:
#         print(n)
#         print("Finished")
#         print(n)
#         return
#     print(n)
#     print_numbers(n - 1)
#     print(n)
#
# print_numbers(10)

# def print_numbers(n):
#     if n == 1:
#         print(n)
#         return
#     print_numbers(n - 1)
#     print(n)
#
# print_numbers(10)

"""
If you print the number before the recursive call, the output will be in descending order — from larger to smaller numbers.
In this case, each function call prints its value first and then makes the recursive call.
So, the numbers keep printing as 10, 9, 8, 7, 6, 5, 4, 3, 2, and finally, when n = 1, the base case is reached, and the smallest number is printed last.
After reaching the base case, backtracking begins — the function starts returning, and all the previous calls that were made before the base case now execute in reverse order, moving back from 1 to 10.

On the other hand, if you print the number after the recursive call, the output will be in ascending order — from smaller to larger numbers.
In this case, when the function is first called with n = 10, the condition n == 1 is not met, so the recursive calls continue silently (nothing is printed yet) until n becomes 1.
When n = 1, the base case is triggered, and 1 is printed.
After that, during backtracking, the remaining numbers — 2, 3, 4, 5, 6, 7, 8, 9, and 10 — are printed one by one as the function returns from each recursive call.

"""

# def walk(n):
#     if n == 1:
#         print(f"Yoy take {n} step")
#         return
#     walk(n - 1)
#     print(f"Yoy take {n} step")
#
# walk(20)
#
# def factorial(n):
#     if n == 0:
#         return 1    # Recursive Approach
#     return n * factorial(n - 1)
#
# print(factorial(5))
#
# def factorial(n):
#      fact =  1
#      for i in range(1, n + 1):  # Iterative Approach
#          fact = fact * i
#      print(fact)
#
# factorial(5)
#
# def open_box(box):
#     if box["next"] is None:          # base case: no more boxes
#         print("🎁 Found the toy! Stop here.")
#         return
#     print("📦 Opening a box...")
#     open_box(box["next"])            # recursive call
#     print("🧩 Closing a box...")
#
# box = {
#     "next" : {
#         "next": {
#             "next": {
#                 "next": {
#                     "next": None
#                 }
#             }
#         }
#     }
# }
# open_box(box)

# Array Traversal using recursion

# def traverse(arr, i = 0):
#      if i == len(arr):
#          return
#      print(arr[i])
#      traverse(arr, i + 1)
#
# arr = [1,2,3,4,5]
# traverse(arr)

#Sum of array elements using recursion

def sum_array(array, i = 0):
    if i == len(array):
        return 0
    result = array[i] + sum_array(array, i + 1)
    return result

arr = [10,20,30,40,50]
print(sum_array(arr))



