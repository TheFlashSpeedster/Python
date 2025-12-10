"""
Q4. Sum of First n Natural Numbers (Easy) 
Use for loop to compute sum of 1...n. 
"""

n = int(input())
total = 0
for i in range(1, n+1):
  total += i

print(total)