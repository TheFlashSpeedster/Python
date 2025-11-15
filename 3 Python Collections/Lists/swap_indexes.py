# Given a list in Python and provided the index of the elements,
# write a program to swap the two elements in the list.

# Examples:
# Input : List = [23, 65, 19, 90], idxl = 0, idx2 =2
# Output : [19, 65, 23, 90]
# Input : List = [1, 2, 3, 4, 5], idxl = 1,idx2=4
# Output : [1, 5, 3, 4, 2]

n = int(input("Size of List:"))
list = []
for _ in range(n):
    list_items = int(input("Enter Number:"))
    list.append(list_items)

print(list)

# Asking user for which Indexes to Swap
print("Enter Indexes for Swapping")
idx1 = int(input("Index1:"))
idx2 = int(input("Index2:"))

# Swapping items at index1 and index2
temp = list[idx1] # Store value to index1 into temp
list[idx1] = list[idx2] # Replace item at idx1 with idx2
list[idx2] = temp # Replace idx2 with original idx1 item
print(list)