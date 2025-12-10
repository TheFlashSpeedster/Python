"""
# Read & Print File Content

A text file data.txt contains:
Hello Python
Welcome to File Handling
Write a Python program to read this file and print all lines.
"""

file = open("/Users/atul/Desktop/Backend/Python/Errors & Exceptions/Questions/q1/text.txt", "r")
content = file.read()
print(content)
file.close()