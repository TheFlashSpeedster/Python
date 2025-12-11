"""
Q6. Count Digits of a Number (Medium) 
Use while loop to count digits in an integer.
"""

n = int(input())
count = 0
x = n

while x>0:
  count += 1
  x = x // 10

print(count)