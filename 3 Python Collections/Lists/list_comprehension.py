# list Comprehenshion
# When we want to make a new list from items of an existing list

list = [10, 20, 30, 40, 50]
print(list)

# Add (items > 25) in new_list
new_list = [i for i in list if i > 25]
print(new_list)

# EXAMPLE - FRUITS LIST
fruits = ["banana", "apple", "orange", "mango", "guava"]
print(fruits)

# Add items which contains "o"
new_fruits = [j for j in fruits if "o" in j]
print(new_fruits)

# Copying List
fruits1 = ["banana", "apple", "orange"]
fruits2 = fruits1.copy()
print(fruits1)
print(fruits2)

# Concatination of Lists
list1 = [10, 20, 30]
list2 = [40, 50]
list3 = list1 + list2
print(list3)