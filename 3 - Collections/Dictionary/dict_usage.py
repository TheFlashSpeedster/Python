# Creating Dictionary
dict = {"John": 25, "Alex": 66, "Harry": 47}
print(dict)

# Datatype/class
print(type(dict))

# Length of Dict
print(len(dict))

# Access items of dict
print(dict["John"]) # M1 - Print Value for key "John"
print(dict.get("Harry")) # M2 - Print Value for key "Harry"

print(dict.keys()) # Print all Keys

# Updating Value of Key
numbers = {"One": 10,"Two": 20}
print(numbers)

numbers["One"] = 1
numbers["Two"] = 2
print(numbers)

# Add Items
users = {"John": 25, "Alex": 66, "Harry": 47}
print(users)

users["Martin"] = 52
print(users)

# Joining Dicts
phones1 = {"Apple": 1, "Ball": 2, "Cat": 3}
phones2 = {"Dog": 4, "Egg": 5, "France": 6}
print(phones1)

phones1.update(phones2)
print(phones1)

# Remove Items

## M1 - Using pop(index)
dict1 = {"John": 25, "Alex": 66, "Harry": 47}
print(dict1)

dict1.pop("Alex") # Remove spcific item (key-value pair)
print(dict1)

## M2 - Using popitem() (removes only latest pair)
dict2= {"John": 25, "Alex": 66, "Harry": 47}
print(dict2)

dict2.popitem() # Removes latest pair
print(dict2) # Removes Harry

## Empty the Dict

dict3 = {"John": 25, "Alex": 66, "Harry": 47}
print(dict3)

dict3.clear() # Remove All Items from Dictionary
print(dict3)

# Print Values of a Dict
dict4 = {"John": 25, "Alex": 66, "Harry": 47}
print(dict4)

print(dict4.keys()) # Print All Keys
print(dict4.values()) # Print All Values

for i in dict4:
    print(i) # Print Keys
    print(dict4[i]) # Print Values

for j in dict4.items(): # Print Key with Value (As Tuple Pairs)
    print(j)

for x, y in dict4.items(): # Print Keys & Values (As Direct Output)
    print(x, y)


# Nested Dictionaries

nested_dict = {
    "Area1" : {
        "x" : 0,
        "y" : 1,
        "z" : 2
    },
    "Area2" : {
        "a" : 3,
        "b" : 4,
        "c" : 5
    }
}

print(nested_dict)

print(nested_dict["Area1"]["x"]) # Value of x in Area1
print(nested_dict["Area2"]["b"]) # VAlue of b in Area2