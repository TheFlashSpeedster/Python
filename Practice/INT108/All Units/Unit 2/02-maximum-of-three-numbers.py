"""
Q2. Maximum of Three Numbers (Easy–Medium) 
Find largest among three numbers using if–elif–else.
"""

a = int(input())
b = int(input())
c = int(input())

if a>=b and a>=c:
  print(a)
elif b>=a and b>=c:
  print(b)
else:
  print(c)