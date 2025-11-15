'''
Given a dictionary in Python, write a Python program to find the
sum of all items in the dictionary.

Input : {'a': 100, 'b': 200, 'c': 300}
Output : 600

Input : {'x': 25, 'y':18, 'z':45}
Output : 88
'''

# M1
dict1 = {"a" : 100,
        "b" : 200,
        "c" : 300}

a = dict1["a"]
b = dict1["b"]
c = dict1["c"]

print("Sum is:", a+b+c)

# M2
dict2 = {"a" : 100,
        "b" : 200,
        "c" : 300}

print(dict2.values()) # Print All Values

print("Sum is:", sum(dict2.values())) # Sum of All Values