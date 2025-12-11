"""
7. Recursively find the factorial of a natural number.
"""

n = int(input("Enter Number: "))

def fac(n):
  if n==1:
    return 1
  return n*fac(n-1)

print(fac(n))