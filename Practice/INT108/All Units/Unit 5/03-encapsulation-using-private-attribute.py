"""
Q3. Encapsulation using Private Attribute (Medium) 
Create class BankAccount with private attribute __balance and methods deposit, withdraw, 
get_balance. 
"""

class BankAccount:
  def __init__(self, balance):
    self.__balance = balance # private attribute (cannot be accessed directly, but can be accessed by methods of same class)

  def deposit(self, amount):
    self.__balance += amount
  
  def withdraw(self, amount):
    if self.__balance >= amount:
      self.__balance -= amount
    else:
      print("Insufficient Balance")
  
  def get_balance(self):
    print("Balance:", self.__balance)

user1 = BankAccount(1000) # set initial balance
user1.deposit(200) # deposit amount
user1.withdraw(10000) # withdraw amount
user1.get_balance() # check balance
  