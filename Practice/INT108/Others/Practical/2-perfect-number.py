"""
2. Write a program to find whether an inputted number is perfect or not.
"""

n = int(input("Enter Number: "))

# perfect number - whose sum of all divisors (except number itself) is equal to the number 

total = 0
for i in range(1, n):
  if n%i==0:
    total += i

if total==n:
  print("Perfect Number")
else:
  print("Not Perfect")