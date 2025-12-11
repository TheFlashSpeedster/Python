"""
# Find Longest Word in a File

Given a file words.txt containing multiple words, write a Python program to find the longest word and print it.
"""

file = open("Errors & Exceptions/Questions/q6/words.txt", "r")
words = file.read().split() # list of words
longest_word = max(words, key=len) # max, order by len (length)

print("Longest Word:", longest_word)
