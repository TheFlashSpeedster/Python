# Rectangle - Area & Perimeter

"""
Write a Python class named Rectangle to represent a rectangle shape.
The class should have the following functionalities:

1. A method named set_dimensions that takes two parameters width and height and sets the attributes of the rectangle object accordingly.

2. A method named area that calculates and returns the area of the rectangle

3. A method named perimeter that calculates and returns the perimeter of the rectangle

Use this to create objects of the class and print the width, height, area and perimeter.

"""

class Rectangle:
  def set_dimensions(self, width, height):
    self.width = width
    self.height = height

  def area(self):
    total_area = (self.width*self.height)
    return total_area
  
  def perimeter(self):
    total_perimeter = 2*(self.width + self.height)
    return total_perimeter

# Creating Objects
data1 = Rectangle()

# Set Dimensions in the Class
data1.set_dimensions(10,2)

# Print Dimensions
print(f"Width = {data1.width}\nHeight = {data1.height}")

# Print Area
print(f"Area = {data1.area()}") # Calling area() function

# Print Perimeter
print(f"Perimeter = {data1.perimeter()}") # Calling perimeter() function