"""
Q3. Sum of List using Function (Easy–Medium) 
Write function list_sum(lst) that returns sum of elements.
"""

def list_sum(lst):
  total = 0
  for i in lst:
    total += i
  return total

lst = [1, 2, 3]
print(list_sum(lst))