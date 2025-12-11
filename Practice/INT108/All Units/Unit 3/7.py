"""
Q7. Recursive Fibonacci (Medium–High) 
Return nth Fibonacci number using recursion.
"""

def fib(n):
  if n<=1:
    return n
  return fib(n-1) + fib(n-2)

print(fib(6))