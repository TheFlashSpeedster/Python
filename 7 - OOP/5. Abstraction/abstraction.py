# Abstraction
# Abstraction is the concept of hiding the complex implementation details and showing only the essential features of the object.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side
    
# Creating Objects

## rectangle object
rect = Rectangle(10, 5)
print(f"Rectangle Area: {rect.area()}")
print(f"Rectangle Perimeter: {rect.perimeter()}")

## square object
sq = Square(4)
print(f"Square Area: {sq.area()}")
print(f"Square Perimeter: {sq.perimeter()}")

# Note: You cannot create an instance of an abstract class directly.