# Creating a Set
set = {10, 20, 30, 40, 50}
print(set)

# Datatype/class of Set
print(type(set))

# Length of Set
print(len(set))

# Accessing Items in Set
for i in set:
    print(i) # Print all items

# Check if an item exists in Set

## M1
if 20 in set:
    print("20 is Present")

## M2 - Boolean Result
print("20:", 20 in set)

# Adding items in Set
set1 = {10, 20, 30, 40, 50}
set1.add(60) # Adding new unique item
print(set1)

set1.add(30) # Adding Duplicate item
print(set1) # Only One 30 gets Printed

# Add another sequence (list/tuple/set) in a Set
names_set = {"red", "yellow"}
names_list = ["apple", "ball"]
print(names_set)

names_set.update(names_list)
print(names_set)

# Removing items from Set
fruits_set = {"orange", "banana", "papaya"}
print(fruits_set)

fruits_set.remove("banana")
print(fruits_set)


# fruits_set.remove("kiwi") # Shows error if item is absent in set
# print(fruits_set)

fruits_set.discard("guava") # No Error if item is absent in set
print(fruits_set)


# Joining Sets
s1 = {"a", "b", "c"}
s2 = {"d", "e", "a"}
print(s1, s2)

s3 = s1.union(s2) # union - s3 items = s1 items with s2 items
print(s3)

s1.update(s2) # update - s2 items gets added into s1
print(s1)

## keep only duplicate/common items from set
s1.intersection_update(s2) # intersection_update - selects common items and updates s1
print(s1)

## Keep all items except duplicate/common items
## Only keep Unique Items
s1.symmetric_difference_update(s2)
print(s1)