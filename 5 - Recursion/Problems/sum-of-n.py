# Sum of Numbers from 1 to N

def sum(n):
  if n==1:
    return 1
  return n + sum(n-1)

n = int(input("Number: "))
print(sum(n))