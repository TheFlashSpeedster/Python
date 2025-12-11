"""
Q7. Operator Overloading (__add__) (High) 
Overload + to add two Point objects.
"""

class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)
  
p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2
print(p3.x, p3.y)