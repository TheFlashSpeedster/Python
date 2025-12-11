"""
Q4. Single Inheritance (Medium) 
Create base class Person and derived class Employee adding salary. 
"""

class Person:
  def __init__(self, name):
    self.name = name

  def show(self):
    print("Name:", self.name)

class Employee(Person):
  def __init__(self, name, salary):
    super().__init__(name) # inherit __init__() method
    self.salary = salary

  def show(self):
    super().show() # inherit show() method
    print("Salary:", self.salary)

e1 = Employee("Tony", 10)
e1.show()

