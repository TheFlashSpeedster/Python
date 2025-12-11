"""
Q7. Tuple as Return Value (Medium) 
Write function that takes two numbers and returns (sum, difference, product) as tuple.
"""

def operation(a, b):
  tuple1 = []
  tuple1.append(a+b)
  tuple1.append(a-b)
  tuple1.append(a*b)

  return tuple(tuple1)

print(operation(2, 3))
