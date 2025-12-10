class Account:
  def __init__(self, balance, accno):
    self.balance = balance
    self.accno = accno

  def debit(self, amount):
    self.balance -= amount
    print("Balance:", self.balance)
  def credit(self, amount):
    self.balance += amount
    print("Balance:", self.balance)

acc1 = Account(1000, 123)
acc1.debit(200)
acc1.credit(100)