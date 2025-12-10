import re

st = "Hello World Hello 123 %$2"

# re_findall = re.findall(r"Hello", st)
# print("findall", re_findall)

# re_match = re.match(r"Hello", st)
# print("match", re_match.group())

# \d - digits
# \D - non-digits
# \w - alphanumeric (digits and alphabets)
# \W - non alphanumeric (digits and alphabets)
re_digits = re.findall(r'\d', st)
print(re_digits)
