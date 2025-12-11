"""
Q6. try–except–else–finally (Medium–High) 
Demonstrate all four parts.
"""

try:
  n = int(input("Enter Number: "))

except ValueError:
  print("Not an integer")

else:
  print("Number is", n)

finally:
  print("Program Finished!")