"""
# Count Number of Lines in a File

Given a file example.txt, write code to count and print the total number of lines.
"""

file = open("Errors & Exceptions/Questions/q5/example.txt", "r")
count = len(file.readlines())
print("No of lines:", count)

