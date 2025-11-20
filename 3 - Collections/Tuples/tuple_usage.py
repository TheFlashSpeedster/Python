# Creating a Tuple
colours = ("red", "green", "blue")
print(colours)

# Special Way of Creating Tuple
tuple1 = tuple(("orange", "yellow", "pink"))
print(type(tuple1))

# Tuple with 1 Item
colours = ("apple",) # colours = ("apple") - this is string
print(colours)

# Datatype/class of Tuple
print(type(colours))

# Length of Tuple
print(len(colours))

# Accessing Items in Tuple
tuple2 = (10, 20, 30, 40, 50)
print(tuple2[0]) # 10
print(tuple2[1]) # 20
print(tuple2[-1]) # 50
print(tuple2[1:3]) # 20 30

# Check if an items exists in tuple

## M1
print("Orange: ", "orange" in tuple1)

## M2
if "orange" in tuple1:
    print("Orange is Present")

# Traverse the Tuple - Print all items per line

for i in tuple1:
    print(i)

# Concatinate Tuples

tuple_a = ("red", "blue")
tuple_b = ("green", "yellow")

tuple_c = tuple_a + tuple_b
print(tuple_c)

# Unpacking Tuples - Assigning Vars to Items

tuple_x = ("orange", "yellow", "pink")
x, y, z = tuple_x # x1 = item at index 0, etc...
print(x) # orange
print(y) # yellow
print(z) # pink