"""
Array Operation: Sorting

Sorting means arranging elements in order, either
ascending (small → big) or descending (big → small).

Types of Sorting Algorithms:

Bubble Sort:
      Compare each pair of adjacent elements and swap them
      if they’re in the wrong order.
      Repeat this until the array becomes sorted.
Selection Sort:
      Selection Sort finds the smallest element in the array
      and puts it at the beginning, then repeats the process
      for the remaining unsorted part.
Insertion Sort:
      Start from the 2nd element.
      Compare it with elements before it.
      Insert it at the correct position in the sorted part
        (left side).
      Repeat for all elements.
"""

# Example

import random

arr = [random.randint(1, 120) for i in range(101)]

print(arr)

# Sorting
# arr.sort() # By-Default it sorts it Ascending Order(S - B)
arr.sort(reverse=True) # To sort it in Descending Order(B - S)
print(arr)

