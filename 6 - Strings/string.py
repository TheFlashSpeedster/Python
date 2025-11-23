# String — concise syntax lines followed by example code

# Basic string literals
# Syntax: s = 'text'  or  s = "text"  or  s = '''multi-line'''
single = 'Hello, World!'
double = "Hello, World!"
triple = '''Hello,
World!'''
print(single)
print(double)
print(triple)

# Concatenation
# Syntax: s3 = s1 + s2
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Indexing and slicing
# Syntax: s[i] -> char, s[start:end] -> substring, s[start:end:step] -> substring with step
idx = "Python"
print(idx[0])        # P
print(idx[-1])       # n
print(idx[1:4])      # yth
print(idx[::-1])     # reverse

# Traversal
# Syntax: for ch in s: ...
t = "Hello"
for ch in t:
  print(ch)
# Syntax: while i < len(s): ...
i = 0
while i < len(t):
  print(t[i])
  i += 1
# Syntax (list comp): [ch for ch in s]
chars = [ch for ch in t]
print(chars)

# Sample string for methods
sample = "  Hello, World! Welcome to Python Programming.  "

# Length
# Syntax: len(s) -> int
print(len(sample))

# Case transformations (return new string)
# Syntax: s.lower(), s.upper(), s.title(), s.capitalize(), s.swapcase()
print(sample.lower())
print(sample.upper())
print(sample.title())
print(sample.capitalize())
print(sample.swapcase())

# Strip and whitespace
# Syntax: s.strip(), s.lstrip(), s.rstrip()
print(sample.strip())
print(sample.lstrip())
print(sample.rstrip())

# Replace
# Syntax: s.replace(old, new[, count])
print(sample.replace("Python", "Java"))
print(sample.replace("o", "0", 1))

# Split and join
# Syntax: s.split(sep), sep.join(list)
words = sample.split()        # default splits on whitespace
print(words)
print("-".join(words))

# Searches and counts
# Syntax: s.find(sub) -> index or -1, s.index(sub) -> index or ValueError, s.count(sub) -> int
print(sample.find("Python"))
print(sample.index("Welcome"))
print(sample.count("o"))

# Starts/ends checks
# Syntax: s.startswith(prefix), s.endswith(suffix)
print(sample.startswith("  Hello"))
print(sample.endswith("Programming.  "))

# Character type checks
# Syntax: s.isalpha(), s.isdigit(), s.isalnum()
alpha_sample = "Hello"
digit_sample = "12345"
alnum_sample = "Hello123"
print(alpha_sample.isalpha())
print(digit_sample.isdigit())
print(alnum_sample.isalnum())
