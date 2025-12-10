"""
Q10. Using try–except–finally
Write code that asks the user to enter age.
If age < 0 → raise ValueError.
Use try-except-finally to handle.
"""

def verifyAge(age):
  if age<0:
    raise ValueError("Age Must Be >=0")

try:
  age = int(input("Enter Age: "))
  verifyAge(age)
  
except ValueError as e:
  print(e)

finally:
  print("Program Finished!")