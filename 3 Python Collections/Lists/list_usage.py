# Creating a List
fruits = ["apple", "mango", "banana", "orange"]

# Special Way of Creating List
colours = list["orange", "yellow", "pink"]
print(type(colours))

print(fruits) # Print List Items

print(type(fruits)) # Check datatype/class

print(len(fruits)) # Count Items

# Check if an item is present in list
# Membership Operator - "in"

print("mango" in fruits) # True
print("kiwi" not in fruits) # True

# OR

if "banana" in fruits:
    print("Banana is Present")
if "kiwi" not in fruits:
    print("Kiwi is Absent")