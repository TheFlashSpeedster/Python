# del (keyword)
# Used to delete object properties or object itself

class Student:
  def __init__(self, name):
    self.name = name

s1 = Student("Tony")
print(s1.name)

del s1.name # delete property of object
print(s1.name) # error

del s1 # delete object
print(s1) # error