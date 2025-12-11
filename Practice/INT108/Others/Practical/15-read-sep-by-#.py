"""
15.Read a text file line by line and display each word separated by a #
"""

with open("Practice/INT108/Others/Practical/sample15.txt", "r") as file:
  words = file.read().split()

print("#".join(words))