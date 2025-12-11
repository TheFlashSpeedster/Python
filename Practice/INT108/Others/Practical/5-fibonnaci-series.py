"""
5.Write a Program to enter the number of terms and to print the Fibonacci Series.
"""

n = int(input("Enter number of terms: "))

a = 0
b = 1

print(a) # 1st
print(b) # 2nd

for i in range(2, n):
  a = b
  b = a+b # swap b with a, and b with (a+b)
  print(b)