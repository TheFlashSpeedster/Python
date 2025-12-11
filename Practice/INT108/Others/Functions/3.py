"""
Q3. Function with *args

Write a function average(*nums) that returns the average of numbers.
"""

def average(*n): # variable parameters
  avg = sum(n)/len(n)
  return avg

print(average(1,2,3))