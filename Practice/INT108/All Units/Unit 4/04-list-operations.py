"""
Q4. List Operations (Easy–Medium) 
Given list of integers, remove all even numbers. 
"""

lst1 = [1, 2, 3, 4, 5, 6]

for i in lst1:
  if i%2==0:
    lst1.remove(i)

print(lst1)