class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

  def average(self):
    total_marks = sum(self.marks)
    total_subjects = len(self.marks)
    avg = total_marks / total_subjects
    print(f"Name: {self.name}\nAverage: {avg}")

s1 = Student("Tony", [99, 98, 97, 100, 100])
s1.average()

s1.name = "Thor"
s1.marks[0] = 0
s1.average()