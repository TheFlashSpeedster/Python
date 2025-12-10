"""
# Copy Content From One File to Another File

Write a Python program to read content from source.txt and copy it into destination.txt.
"""


# Read source.txt and store into "content" variable

file_source = open("Errors & Exceptions/Questions/q4/source.txt", "r") # Open File (read mode)
content = file_source.read() # Store text
file_source.close() # Close File

# Write destination.txt and write content into it
file_dest = open("Errors & Exceptions/Questions/q4/destination.txt", "w") # Open file (write mode)
file_dest.write(content) # write content (replace if any text already exists)
file_dest.close() # Close File
