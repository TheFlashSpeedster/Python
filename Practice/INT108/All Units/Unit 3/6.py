"""
Q6. Recursive Factorial (Medium) 
Write recursive function fact(n).
"""

def factorial(n):
  if n==1:
    return 1
  return n*factorial(n-1)

print(factorial(3))
  