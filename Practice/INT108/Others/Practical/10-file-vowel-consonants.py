"""
10.Read a text file and display the number of vowels/consonants/uppercase/lowercase characters in
the file.
"""

with open("Practice/INT108/Others/Practical/sample10.txt", "r") as file:
  content = file.read() # list of characters
  content = content.replace(" ", "")
  characters = list(content)

vowels_count = 0
consonants_count = 0
uppercase_count = 0
lowercase_count = 0

for i in characters:
  if i in "aeiouAEIOU":
    vowels_count += 1
  elif i.isalpha():
    consonants_count += 1
  if i.isupper():
    uppercase_count += 1
  elif i.islower():
    lowercase_count += 1

print(vowels_count)
print(consonants_count)
print(uppercase_count)
print(lowercase_count)