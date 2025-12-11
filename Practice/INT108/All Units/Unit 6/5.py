"""
Q5. Division with Exception Handling (Easy–Medium) 
Take two numbers and divide, handle ZeroDivisionError.
"""

a = int(input())
b = int(input())

try:
  result = a/b
  print(result)

except ZeroDivisionError:
  print("Cannot divide by zero")