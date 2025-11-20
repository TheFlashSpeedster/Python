# Sum of numbers till N (from 1 to n)

def sum(n):
  total = 0
  for i in range(1, n+1):
    total += i
  print(total)

n = int(input("N: "))
sum(n)