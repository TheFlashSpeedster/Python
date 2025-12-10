"""
# Count Number of Words in a File

Given a file story.txt containing a short paragraph, write a program to count how many words are present in the file.
"""

file = open("/Users/atul/Desktop/Backend/Python/Errors & Exceptions/Questions/q2/story.txt", "r")
content = file.read().split()
words = len(content)
print(words)