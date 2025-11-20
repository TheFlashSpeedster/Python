# Pass By Reference
## In Python, mutable types like lists, dictionaries, and sets are passed by reference.
## This means that when you pass such an object to a function, a reference to the original object is passed.

def fn(list1):
  list1.append(4)
  return list1

list1 = [1,2,3]
print(list1) # [1,2,3] - Original List
print(fn(list1)) # [1,2,3,4] - Inside Function
print(list1) # [1,2,3,4]- Modified Original List

# However, if we reassign the parameter to a new object, the original object remains unchanged.

def fn(list2):
  list2 = [7,8,9] # Reassigning list2 to a new list
  return list2

list2 = [1,2,3]
print(list2) # [1,2,3] - Original List
print(fn(list2)) # [7,8,9] - Inside Function
print(list2) # [1,2,3]- Original List remains unchanged