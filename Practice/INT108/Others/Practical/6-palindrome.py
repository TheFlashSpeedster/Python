"""
6. Write a Program to enter the string and to check if it’s palindrome or not using loop.
"""

st = input("Enter String: ")
rev = ""
for ch in st:
  rev = ch + rev

if st == rev:
  print("Palindrome")
else:
  print("Not Palindrome")