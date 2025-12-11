"""
Q10. Pattern Printing (Medium–High) 
For n=4, print: 
* 
* * 
* * * 
* * * *
"""

n = 4

for i in range(n):
  for j in range(i+1):
    print("*", end=" ")
  print()