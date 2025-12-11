"""
Q9. Higher-Order Function (High) 
Write function apply_twice(f, x) that applies function f two times
"""

def apply_twice(f, x):
  return f(f(x))

def inc(n):
  return n+1

print(apply_twice(inc, 5))