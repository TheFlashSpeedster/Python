# Escape Characters in Strings

r"""
\' or \" - Single or Double Quote
\\ - Backslash
\n - New Line
\r - Carriage Return
\t - Tab
\b - Backspace
\f - Form Feed
\v - Vertical Tab
\ooo - Octal value
\xhh - Hexadecimal value
"""

# 1. Single or Double Quote - \' or \"
str1_a = 'He\'s Great!'
str1_b = "He\"s Great!"
print(str1_a, str1_b)

# 2. New Line - \n
str2 = "Good\nMorning"
print(str2)

# 3. Tab - \t
str3 = "Name:\tJohn\nAge:\t30"
print(str3)

# 4. Backslash - \\
str4 = "This is a backslash: \\"
print(str4)

# 5. Carriage Return - \r
str5 = "Hello World\rPython\rDIE"
print(str5)
