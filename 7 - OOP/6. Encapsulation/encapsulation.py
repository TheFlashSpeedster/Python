# Encapsultion
# It describes bundling data and methods that operate on that data within a single unit or class.

class Student:
  def __init__(self, name, age): # Constructor to initialize attributes
    self.__name = name      # Private Attribute
    self.__age = age        # Private Attribute

  def set_name(self, name): # Setter Method
    self.__name = name

  def get_name(self):       # Getter Method
    return self.__name

  def set_age(self, age):   # Setter Method
    if age >= 0:           # Basic Validation
      self.__age = age

  def get_age(self):        # Getter Method
    return self.__age
  
# Creating Objects
student1 = Student("Flash", 20)
print(student1.get_name())  # Accessing name via getter
print(student1.get_age())   # Accessing age via getter

# Modifying attributes via setter methods
student1.set_name("Arrow")  # Modifying name via setter
student1.set_age(22)        # Modifying age via setter
print(student1.get_name())  # Accessing modified name via getter
print(student1.get_age())   # Accessing modified age via getter

# Creating another object
student2 = Student("Batman", 25)
print(student2.get_name())  # Accessing name via getter
print(student2.get_age())   # Accessing age via getter

# Modifying attributes via setter methods
student2.set_name("Superman")  # Modifying name via setter
student2.set_age(30)        # Modifying age via setter
print(student2.get_name())  # Accessing modified name via getter
print(student2.get_age())   # Accessing modified age via getter

# Note: Direct access to private attributes like student1.__name or student1.__age will raise an AttributeError