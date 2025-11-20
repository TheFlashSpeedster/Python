# Sum of Numbers from n1 to n2

def sumRange(n1, n2):
  total = 0
  for i in range(n1, n2+1):
    total += i
  print(total)

n1 = int(input("Start Number: "))
n2 = int(input("End Number: "))
sumRange(n1, n2)