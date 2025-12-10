# Methods
# Methods are functions that belongs to objects.

class Student:
  college = "Avengers"
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def greet(self):
    print(f"Hello {self.name}!")

  def get_marks(self):
    print(f"Marks: {self.marks}")

s1 = Student("Tony", 23)
s1.greet()
s1.get_marks()
print(f"College: {s1.college}")

s2 = Student("Tom", 25)
s2.greet()
s2.get_marks()
print(f"College: {s2.college}")