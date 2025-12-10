# Typs of Errors
## Syntax Error
# A syntax error occurs when the code is not written in accordance with the rules of the programming

# language. For example, forgetting a colon at the end of a function definition will raise a syntax error.
# Example:
def my_function()
    print("Hello, World!")  # This will raise a SyntaxError due to the missing colon.
# To fix it, add the missing colon:
def my_function():
    print("Hello, World!")
## Indentation Error
# An indentation error occurs when the code is not properly indented. Python relies on indentation to
# define blocks of code. For example, forgetting to indent the body of a function will raise

# Logical Error
# A logical error occurs when the code runs without crashing but produces incorrect results. This type
# of error is often harder to detect because the program does not raise an exception. For example
def add_numbers(a, b):
    return a - b  # This is a logical error; it should be a + b
# To fix it, correct the operation:
def add_numbers(a, b):
    return a + b
# To fix it, indent the body of the function properly:
def my_function():
    print("Hello, World!")

# Runtime Error
# A runtime error occurs while the program is running. This type of error can be caused by various issues,
# such as dividing by zero or trying to access a file that does not exist. For example:
a = 5
b = 0
def divide_numbers(a, b):
    return a / b  # This will raise a ZeroDivisionError if b is 0
print(divide_numbers(a, b))
# To fix it, you can add a check to prevent division by zero:

s = [1, 2, 3]
print(s[5])  # This will raise an IndexError because index 5 does not exist

x = int("hello")  # This will raise a ValueError because "hello" cannot be converted to an integer
print(x)