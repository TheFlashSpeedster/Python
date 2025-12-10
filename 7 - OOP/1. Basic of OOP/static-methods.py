# Static Methods
# Methods that dont use "self" parameter (works at class level)

class Student:
  def __init__(self, name):
    self.name = name

  @staticmethod
  def hello():
    print("Hello World")

  def greet(self):
    print("Hello", self.name)

s1 = Student("Tony")
s1.greet()
s1.hello()