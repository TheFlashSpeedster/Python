"""
Q9. Handle File Not Found Error
Write a Python program to open unknown.txt.
If the file does not exist, handle the exception and print:
File not found!
"""

try:
  file = open("unknown.txt", "r")
  data = file.read()
  print(data)
  file.close()
except FileNotFoundError:
  print("File not found!")