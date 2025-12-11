"""
9.Remove all the lines that contain the character “a” in a file and write it into another file.
"""

with open("Practice/INT108/Others/Practical/source9.txt", "r") as file:
  lines = file.readlines() # list of lines

final = [] # list of lines without "a"
for line in lines:
  if not "a" in line:
    final.append(line)
content = "".join(final) # string

with open("Practice/INT108/Others/Practical/target9.txt", "w") as target:
  target.write(content)