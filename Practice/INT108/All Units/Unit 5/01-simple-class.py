"""
Q1. Simple Class (Easy) 
Create class Student with attributes name and age and method display(). 
"""

class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print("Name:", self.name)
    print("Age:", self.age)

student1 = Student("Tony", 43) # set info
student1.display() # get info