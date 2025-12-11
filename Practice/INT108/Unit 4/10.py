"""
Q10. Copy vs Alias in Lists (High – concept) 
Demonstrate aliasing and copying of a list.
"""

# ----------------------------------------
# Aliasing a List - Giving nicknames
# ----------------------------------------
list1 = [1, 2, 3]
print("List1: ", list1)

list2 = list1 # alias of list1
print("List2: ", list2)

list2.pop(0) # removes in list1 also
print("List1: ", list1)
print("List2: ", list2)

# ----------------------------------------
# Copying a List - Making identical copies
# ----------------------------------------
list1 = [1, 2, 3]
print("List1: ", list1)

list2 = list1[:] # copy of list1
print("List2: ", list2)

list2.pop(0) # list1 remains unchanged
print("List1: ", list1)
print("List2: ", list2)