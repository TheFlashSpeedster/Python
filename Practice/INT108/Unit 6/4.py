"""
Q4. Handle File Not Found Exception (Medium) 
Try to open a file given by user; if it doesn’t exist, print proper message.
"""

filename = input("Filename: ")

try:
  with open(filename, 'r') as file:
    content = file.read()
    print(content)

except FileNotFoundError:
  print("File not found")