"""
Q9. Dictionary Operations (Medium) 
Store names and marks of 3 students in a dictionary and print name of student with highest marks.
"""
student = {}
for i in range(3):
  name = input()
  marks = int(input())
  student[name] = marks
print(student.items())
topper = max(student, key=student.get)
print("Topper:", topper)
print("Marks:", student[topper])