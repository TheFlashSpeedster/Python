"""
Q7. Tuple as Return Value (Medium) 
Write function that takes two numbers and returns (sum, difference, product) as tuple.
"""

def operation(a, b):
  list1 = []
  list1.append(a+b)
  list1.append(a-b)
  list1.append(a*b)

  return tuple(list1)

print(operation(2, 3))
