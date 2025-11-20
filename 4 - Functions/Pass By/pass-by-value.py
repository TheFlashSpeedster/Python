# Pass By Value
## In Python, immutable types like integers, strings, and tuples are passed by value.
## This means that when you pass such an object to a function, a copy of the object is made.

def fn(x):
    x = x + 10 # Modify x value (inside function)
    return x

x = 5
print(x) # 5 - Original Value
print(fn(x)) # 15 - (Inside Function)
print(x) # 5 - Original Value remains unchanged