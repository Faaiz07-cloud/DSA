"""
Pointers in array confuse many beginners, especially if you’re coming from Python,
because Python doesn’t have pointers explicitly, but in C / C++, pointers and arrays
are deeply connected.

Pointer = Address

arr = [10, 20, 30]

Index	                 Value	                    Address (Pointer)
0	                      10	                           1000
1	                      20	                           1004
2	                      30	                           1008

=> “These numbers (addresses) are automatically generated, not like 1000 or 1004 —
they’re stored in memory and shown in hexadecimal.”

There is a Formula to find the address of a specific value:
                = Base Address + Value * Data-Type(Bytes)

To find the base address
arr = [10, 20, 30, 40, 50]

print(id(arr)) # address of list object (not elements)
print(id(arr[1])) # address of first element

Pointer stores the address of an element.
"""

