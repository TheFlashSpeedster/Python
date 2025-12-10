"""
Write a Python function that checks if the given string is a palindrome or not.

Input: maam
Output: True
"""

# str = input("String: ")

# final_str = str.replace(" ", "").lower()

# if final_str == final_str[::-1]:
#   print("Palindrome: Yes")
# else:
#   print("Palindrome: No")

def palindrome(str):
  final_str = str.replace(" ", "").lower()
  
  final_str_reversed = final_str[::-1]
  if final_str == final_str_reversed:
    print("Palindrome: Yes")
  else:
    print("Palindrome: No")

str = " M  a aaA m   "
palindrome(str)