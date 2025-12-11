"""
Q10. Copy Content from One File to Another (Medium) 
Read from source.txt and write to target.txt. 
"""

with open("Practice/INT108/Unit 6/source10.txt", "r") as source:
  content = source.read()

with open("Practice/INT108/Unit 6/target10.txt", "w") as target:
  target.write(content)