# Reverse a Tuple

# Input : tuples = ('z','a','d','f','g','e','e','k')
# Output : ('k', 'e', 'e', 'g', 'f', 'd', 'a', 'z')
# 4

# Input : tuples = (10, 11, 12, 13, 14, 15)
# Output : (15, 14, 13, 12, 11, 10 

input_list = input("Enter Data:")

list = []

# Adding value in reverse order
for i in reversed(input_list):
    list.append(i) # append values in list in reverse order

print(list)

output_tuple = tuple(list) # Convert list to tuple
print(output_tuple) # print final list as tuple