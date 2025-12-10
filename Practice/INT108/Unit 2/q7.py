"""
Q7. Menu-Driven Calculator (Medium–High) 
Create menu: 1.Add 2.Subtract 3.Multiply 4.Divide. Use while loop until user chooses exit.
"""

while True:
  print("1.Add 2.Subtract 3.Multiply 4.Divide 5.Exit")
  choice = int(input("Choice: "))

  if choice == 5:
    break

  a = int(input("First Number: "))
  b = int(input("Second Number: "))

  if choice == 1:
    print(a+b)
  
  elif choice == 2:
    print(a-b)
  
  elif choice == 3:
    print(a*b)
  
  elif choice == 4:
    print(a/b)

  else:
    print("Invalid Choice")


