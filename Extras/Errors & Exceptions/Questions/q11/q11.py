"""
Q11. Multiple Exceptions Handling
Write a Python program to perform:
result = a / b
Handle ZeroDivisionError and TypeError separately.
"""

def division(a,b):
  result = float(a)/float(b)
  print(result)

a = input("Enter 1st Number: ")
b = input("Enter 2nd Number: ")

try:
  division(a, b)

except ZeroDivisionError:
  print("Cannot Be Divided By Zero")

except ValueError:
  print("Only Integers are Allowed!")