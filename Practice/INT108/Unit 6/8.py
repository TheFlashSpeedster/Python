"""
Q8. Find All Email IDs in Text (High) 
Use regex to extract all email IDs from a given text string.
"""

import re

text = "Contact: abc@example.com and info@test.org"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

emails = re.findall(pattern, text)
print(emails)