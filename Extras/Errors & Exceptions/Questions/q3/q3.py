"""
# Write & Append to File

Write a Python program that:
1. Creates a file notes.txt
2. Writes the line: "Python is easy."
3. Appends another line: "File handling is useful."
"""

# Write And Append New Content To notes.txt
file = open("/Users/atul/Desktop/Backend/Python/Errors & Exceptions/Questions/q3/notes.txt", "a")
file.write("\nFile handling is useful.")
file.close()

# Print notes.txt
file = open("/Users/atul/Desktop/Backend/Python/Errors & Exceptions/Questions/q3/notes.txt", "r")
content = file.read()
print(content)
file.close()