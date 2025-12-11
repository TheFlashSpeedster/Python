"""
Q2. Function Returning Multiple Values

Write a function compute(n) that returns square and cube of n.
"""

def compute(n):
  square = n**2
  cube = n**3
  return square, cube

print(compute(2))