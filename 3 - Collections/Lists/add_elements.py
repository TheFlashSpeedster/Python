# Adding Elements/Items in a List

list = [10, 20, 30]
print(list)

# append() - insert an item at end
list.append(40)
print(list)

# insert() - insert item at an index
list.insert(2, 25)
print(list)

# extend() - add list2 in list1
list1 = [10, 20, 30]
list2 = [40, 50, 60]
print(list1)

list1.extend(list2)
print(list1)