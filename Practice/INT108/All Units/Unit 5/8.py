"""
Q8. Class Variable vs Instance Variable (Medium–High) 
Create class Counter with class variable count that tracks how many objects are created.
"""

class Counter:
  count = 0
  def __init__(self):
    Counter.count += 1

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
print(Counter.count)