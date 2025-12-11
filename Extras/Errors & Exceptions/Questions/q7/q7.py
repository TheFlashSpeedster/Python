"""
Q7. Handle Division by Zero
Write a Python program to take two numbers from the user and handle the case where the user enters 0 as denominator.
"""

try:
  n1 = int(input("Enter 1st Number: "))
  n2 = int(input("Enter 2nd Number: "))
  print(n1/n2)

except ZeroDivisionError:
  print("Denominator Can't Be Zero")