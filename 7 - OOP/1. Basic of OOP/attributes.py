# Class & Instance Attributes
# Class attributes are shared by all instances of the class. They can be accessed using the class name or any instance of the class.
# Instance/Object attributes are unique to each instance of the class. They are typically defined within methods using the self parameter.

class Student:
  college = "ABC College" # Class Attribute (Same for all objects)

  def __init__(self, name, marks):
    self.name = name # Object Attribute (Unique to each object)
    self.marks = marks # Object Attribute (Unique to each object)

s1 = Student("Alex", 98)
print(s1.name, s1.marks, s1.college)

s2 = Student("Bravo", 56)
print(s2.name, s2.marks, s2.college)

print(Student.college) # Directly Accessing Class Attribute