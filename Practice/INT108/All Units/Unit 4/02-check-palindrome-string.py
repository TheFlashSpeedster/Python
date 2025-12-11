"""
Q2. Check Palindrome String (Easy–Medium) 
Check if given string is palindrome (ignore case).
"""

str1 = input().lower()

if str1 == str1[::-1]:
  print("Palindrome")
else:
  print("Not Palindrome")