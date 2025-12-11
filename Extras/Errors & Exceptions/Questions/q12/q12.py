"""
Q12. Custom Exception Example
Create a program where you define a custom exception LowBalanceError.
Raise it when balance < 500.
"""

class LowBalanceError(Exception):
  pass

balance = int(input("Balance: "))

try:
  if balance<500:
    raise LowBalanceError("Low Balance!")
except LowBalanceError as e:
  print(e)