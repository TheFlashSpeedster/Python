"""
Q8. Exception in Type Conversion
Write a program that asks the user for an integer.
If the user types a non-integer value like "abc", handle the error and print:
Invalid input, please enter a number only.
"""

try:
  n = int(input("Enter Number: "))
  print(n)

except ValueError:
  print("Invalid input, please enter a number only")