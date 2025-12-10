# Access Modifiers in Python OOP

# Access Modifiers are keywords that determine the accessibility of class members (attributes and methods) from outside the class.

# Types of Access Modifiers

# -------------- 1. Public Access Modifier --------------
# Use Normally to Define Public Modifier

class Public:
  def __init__(self):
    self.public_attribute = "This is Public Attribute" # Public Attribute

  def public_function(self): # Public Function/Method
    return "This is Public Function/Method"
  
data1 = Public()
print(data1.public_attribute)
print(data1.public_function())

# -------------- 2. Private Access Modifier --------------
# Use __ (double underscore) to Define Private Modifier

class Private:
  def __init__(self):
    self.__private_attribute = "This is Private Attribute"

  def __private_function(self):
    return "This is Private Function/Method"
  
data1 = Private()
print(data1.__private_attribute) # AttributeError
print(data1.__private_function()) # AttributeError

# Example Code 1 - Private Modifiers
class Account:
  def __init__(self, acc_no, acc_pass):
    self.__acc_no = acc_no # private attribute
    self.__acc_pass = acc_pass # private attribute
  def get_pass(self):
    return "Password: " + self.__acc_pass

acc1 = Account("123", "abcde") # AttributeError
# print(acc1.acc_no, acc1.acc_pass) # AttributeError
print(acc1.get_pass()) # abcde (accessible by function of same class)

# Example Code 2 - Private Modifiers

class Person:
  __name = "Anonymous"
  def __hello(self): # private method
    print("Hello World")

  def welcome(self):
    return self.__hello() # calling private method via another method in same class
  
p1 = Person()
p1.__hello() # AttributeError
p1.welcome() # Hello World

# ------------ 3. Protected Access Modifier --------------
# Use _ (single underscore) to Define Protected Modifier

class Protected:
  def __init__(self):
    self._protected_attribute = "This is Protected Attribute"

  def _protected_function(self):
    return "This is Protected Function/Method"
  
data1 = Protected()
print(data1._protected_attribute)
print(data1._protected_function())