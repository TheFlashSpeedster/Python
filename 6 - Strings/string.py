"""
Strings - Examples and common operations

This module demonstrates:
- String literals (single, double, triple quotes)
- Basic string operations (concatenation, indexing, slicing)
- Traversing strings (for/while/list comprehension)
- Common string methods (transformations, manipulation)
- Searches, counts, and boolean checks for string content
"""

# ---------------------------------------------------------------------------
# 1. STRING LITERALS
# ---------------------------------------------------------------------------

# Basic string literal examples using single, double, and triple quotes.

# Single quotes
single_quote_str = 'Hello, World!'
print(single_quote_str)

# Double quotes
double_quote_str = "Hello, World!"
print(double_quote_str)

# Triple quotes (useful for multi-line strings)
triple_quote_str = '''Hello, World!'''
print(triple_quote_str)

# ---------------------------------------------------------------------------
# 2. STRING OPERATIONS
# ---------------------------------------------------------------------------

# Concatenation
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + str2
print("Concatenated String:", concatenated_str)

# Indexing and slicing
index_str = "Python"
print(index_str[0])     # First character: P
print(index_str[-1])    # Last character: n
print(index_str[2])     # Third character: t
print(index_str[-3])    # Third from the end: h
print(index_str[1:4])   # Substring from index 1 to 3: yth

# ---------------------------------------------------------------------------
# 3. TRAVERSING STRINGS
# ---------------------------------------------------------------------------

# Using for loop
traverse_str1 = "Hello World"
for i in traverse_str1:
  print(i)  # Prints each character on a new line

# Using while loop
traverse_str2 = "Hello World"
index = 0
while index < len(traverse_str2):
  print(traverse_str2[index])  # Prints each character on a new line
  index += 1

# Using list comprehension
traverse_str3 = "Hello World"               # string
traverse_list = [i for i in traverse_str3]  # list of characters
for i in traverse_str3:
  print(i)

# ---------------------------------------------------------------------------
# 4. STRING METHODS (TRANSFORMATIONS & MANIPULATIONS)
# ---------------------------------------------------------------------------

sample_str = "  Hello, World! Welcome to Python Programming.  "

# Inspection
print(len(sample_str))  # Length of the string (includes spaces)

# String transformations (return new string, doesn't modify original)
print(sample_str.lower())       # Convert to lowercase
print(sample_str.upper())       # Convert to uppercase
print(sample_str.title())       # Capitalize first letter of each word
print(sample_str.capitalize())  # Capitalize first letter of the string only
print(sample_str.swapcase())    # Swap case of all characters

# String manipulations (return new string, doesn't modify original)
# strip() - remove leading and trailing whitespace
print(sample_str.strip())

# replace(old, new, count) - replace occurrences of a substring
print(sample_str.replace("Old_String", "New_String"))         # replace all occurrences
print(sample_str.replace("Old_String", "New_String", 2))      # replace first 2 occurrences

# split(separator) - split string into a list by the separator
print(sample_str.split(" "))  # Split by space

# ---------------------------------------------------------------------------
# 5. STRING SEARCHES AND COUNTS
# ---------------------------------------------------------------------------

# len() - length of the string
print(len(sample_str))

# find(substring) - index of first occurrence, -1 if not found
print(sample_str.find("Python"))

# index(substring) - index of first occurrence, raises ValueError if not found
print(sample_str.index("Welcome"))

# count(substring) - count occurrences of a substring
print(sample_str.count("o"))

# ---------------------------------------------------------------------------
# 6. STRING CHECKS (BOOLEAN METHODS)
# ---------------------------------------------------------------------------

# startswith(substring) - whether the string starts with the given substring
print(sample_str.startswith("  Hello"))

# endswith(substring) - whether the string ends with the given substring
print(sample_str.endswith("Programming.  "))

# ---------------------------------------------------------------------------
# 7. CHARACTER TYPE CHECKS (RETURN BOOLEAN)
# ---------------------------------------------------------------------------

# isalpha() - all characters are alphabetic (a-z, A-Z)
print(sample_str.isalpha())

# isdigit() - all characters are digits (0-9)
print(sample_str.isdigit())

# isalnum() - all characters are alphanumeric (letters or digits)
print(sample_str.isalnum())
