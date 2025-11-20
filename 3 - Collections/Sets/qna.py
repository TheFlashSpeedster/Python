'''
Given three arrays, we have to find common elements in three
sorted lists using sets.

Input : arl = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
Output : [80, 20]

Input : arl = [1, 5, 5]
ar2 = [3, 4, 5, 5, 10]
ar3 = [5, 5, 10, 20]
Output : [5]
'''

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

# Convert lists to sets for set operations
set1 = set(ar1)
set2 = set(ar2)
set3 = set(ar3)

# intersection_update() keeps only common elements
set1.intersection_update(set2)
set1.intersection_update(set3)

print(list(set1))  # Convert set to list for output