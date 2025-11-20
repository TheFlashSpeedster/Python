# Print Numbers from N to 1

def num1(n1):
  #base case
  if n1==0:
    return
  
  # print n1
  print(n1) # 5 4 3 2 1
  num1(n1-1) # recursive call

# Input
n1 = int(input("Number: "))

# Call Function
num1(n1)

# Print Numbers from 1 to N

def num2(n2):
  #base case
  if n2==0:
    return
  
  # recursive call
  num2(n2-1)
  print(n2)

n2 = int(input("Number: "))
num2(n2)