"""
Q9. Data Hiding Example (Medium) 
Show that private variable cannot be accessed directly from object. 
"""

class Account:
  def __init__(self, id, pwd):
    self.id = id
    self.__pwd = pwd

user1 = Account(123, "xyz")
print(user1.id) # public attribute/variable
print(user1.__pwd) # private attribute/variable