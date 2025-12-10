"""
Q2. Function with Default Argument (Easy) 
def power(a, b=2) returns a raised to power b.
"""

def power(a, b=2):
  return a**b

a = int(input())
b = int(input())


print(power(a)) # calculate a**2
print(power(a, b)) # calculate a**b