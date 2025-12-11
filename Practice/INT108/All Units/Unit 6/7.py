"""
Q7. Simple Regex – Validate Mobile Number (Medium) 
Check if given string is a valid 10-digit number using regex.
"""
import re

phone = input("Enter Phone Number: ")
pattern = r"^[0-9]{10}$"

if re.match(pattern, phone):
  print("Valid")
else:
  print("Invalid")