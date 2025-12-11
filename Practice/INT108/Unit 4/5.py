"""
Q5. List of Squares (Easy) 
Create list containing squares of numbers 1–10 using list comprehension. 
"""

sq_list1 = []
for i in range(1, 11):
  sq_list1.append(i**2)

print(sq_list1)

# Via list comprehension

sq_list2 = [i**2 for i in range(1, 11)]
print(sq_list2)