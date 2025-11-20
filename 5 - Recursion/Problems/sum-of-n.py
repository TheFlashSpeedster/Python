# Sum of Numbers from 1 to N

def sum(n):
  if n==1:
    return 1
  total = n + sum(n-1)
  return total

n = int(input("Number: "))
print(sum(n))