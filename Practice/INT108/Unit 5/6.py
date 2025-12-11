"""
Q6. Multiple Constructors using Default Arguments (Function Overloading Style) (Medium) 
Create class Point that can be created as Point() or Point(x, y).
"""

class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

point1 = Point(1) # (1 0)
print(point1.x, point1.y)

point2 = Point(4,6) # (4 6)
print(point2.x, point2.y)
