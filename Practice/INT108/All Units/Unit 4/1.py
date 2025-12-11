"""
Q1. Count Vowels in String (Easy) 
Count number of vowels in a string.
"""

str1 = input().lower()

count = 0
for letter in str1:
  if letter in "aeiou":
    count += 1

print("Vowels:", count)