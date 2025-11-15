input_list = input("Enter Data:")

list = []

# Adding value in reverse order
for i in reversed(input_list):
    list.append(i) # append values in list in reverse order

print(list)

output_tuple = tuple(list) # Convert list to tuple
print(output_tuple) # print final list as tuple