# Constructor
## A constructor is a special function that is always invoked/called when an object is created.

# Default Constructor
class Example:
  def __init__(self):
    pass

# Parameterized Constructor
class Example:
  def __init__(self, name):
    self.name = name

# Finding Area of Rectangle

class Rectangle:
  def __init__(self, width, height): # Called Everytime When an Object is Created
    print(f"Width: {width}\nHeight: {height}") # Runs everytime
    self.width = width
    self.height = height

  def area(self):
    result = self.width * self.height
    return result
  
  def perimeter(self):
    result = 2 * (self.width + self.height)
    return result
  
# Creating Objects
data1 = Rectangle(4,3)
print(data1.area())
print(data1.perimeter())

data2 = Rectangle(10,2)
print(data2.area())
print(data2.perimeter())
