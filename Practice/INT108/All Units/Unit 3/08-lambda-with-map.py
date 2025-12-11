"""
Q8. Lambda with map (Medium) 
Given list [1,2,3,4], create new list of squares using lambda.
"""

list1 = [1, 2, 3, 4]

list2 = list(map(lambda x: x**2, list1))

print(list1)
print(list2)