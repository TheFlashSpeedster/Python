"""
Q3. Count Lines in File (Medium) 
Count number of lines in a text file.
"""

with open('Practice/INT108/Unit 6/sample3.txt', 'r') as file:
  lines = file.readlines()

  # Via len()
  n = len(lines)

  # Via For Loop
  # n = 0
  # for i in lines:
  #   n += 1

print(n)