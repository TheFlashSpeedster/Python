"""
Q9. Print Prime Numbers in Range (High) 
Print all prime numbers between 2 and n using nested loops.
"""

n = int(input())

for i in range(2, n):
  prime = True
  if n%i==0:
    prime = False
    break

print(prime)