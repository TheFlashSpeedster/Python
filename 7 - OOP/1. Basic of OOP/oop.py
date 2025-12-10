# Object Oriented Programming (OOP)

# It is a programming paradigm where the software design is organized around data, or objects, rather than functions and logic.

# Classes
# Classes are user-defined data types that act as blueprints/templates for creating objects.

# Objects
# Objects are instances of classes that encapsulate data and behavior related to that data.

class Student: # Defining class
  def set_name(self, name):
    self.name = name
  def get_name(self):
    return self.name
  
# Creating Objects
student1 = Student()
student1.set_name("Flash")
print(student1.get_name())

student2 = Student()
student1.set_name("Arrow")
print(student1.get_name())