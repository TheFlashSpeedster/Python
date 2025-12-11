"""
4.Write a Program to find factorial of the entered number.
"""

n = int(input("Enter Number: "))

f = 1
for i in range(1, n+1):
  f *= i

print("Factorial:", f)