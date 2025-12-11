"""
Q2. Class with Method for Area of Rectangle (Easy–Medium) 
Create class Rectangle with length, breadth and method area().
"""

class Rectangle:
  def __init__(self, length, breadth):
    self.length = length
    self.breadth = breadth

  def area(self):
    result = self.length * self.breadth
    print("Area of Rectangle:", result)


rect1 = Rectangle(2, 3)
rect1.area()