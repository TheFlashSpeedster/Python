# Nested Lists

nested_list = [10, 20, [30, 40], 50]
print(nested_list)

# Prints index2 item
print(nested_list[2]) # [30, 40]

# Prints item at index0 of index2
print(nested_list[2][0]) # 30
 


# EXAMPLE - FRUITS LIST
nested_fruits_list = ["banana", "apple", "orange"]
nested_fruits_list.insert(1, ["mango", "guava"]) # insert at ind1
print(nested_fruits_list)

print(nested_fruits_list[1]) # ['mango', 'guava']
print(nested_fruits_list[1][1]) # guava