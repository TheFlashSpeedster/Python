"""
Q5. Multiplication Table (Easy–Medium) 
Print multiplication table of a number up to 10.
"""

n = int(input())

for i in range(1, 11):
  print(f"{n}*{i} = {n*i}")