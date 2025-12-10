# Inheritence - When a class derives from another class, it inherits all the properties and behaviors of the parent class.
# Child Class Inherits Parent Class's Attributes & Methods/Functions.

# Parent Class

class Parent:
  def __init__(self):
    print("This is Parent Class Print Statement")
    self.parent_attribute = "Hello Attribute from Parent Class"

class Child(Parent): # Child Class Inherits Parent Class
  def __init__(self):
    super().__init__() # Calling Parent Class's __init__ function
    print("This is Child Class Print Statement")
    print(self.parent_attribute) # Accessing Parent Class's Attribute

# Creating Object
## It will call Child Class's __init__ function which in turn calls Parent Class's __init__ function, which prints 1st statement.
## Then, It prints 2nd statement from Child Class's __init__ function.

data1 = Child() 

# Example Codes

class Car:
  color = "Black"
  @staticmethod
  def start():
    return ("Car Started...")

  @staticmethod
  def stop():
    return ("Car Stopped!")

class ToyotaCar(Car):
  def __init__(self, name):
    self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print(car1.name)
print(car1.start()) # Inherits start() method from parent (Car) class
print(car1.color)