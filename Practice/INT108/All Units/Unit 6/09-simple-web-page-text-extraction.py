"""
Q9. Simple Web Page Text Extraction (High – conceptual) 
Assume HTML stored in string html = "<h1>Title</h1><p>Hello World</p>". Extract content between <p> and </p> using regex. 
"""

import re

html = "<h1>Title</h1><p>Hello World</p>"
pattern = re.search(r"<p>(.*?)</p>", html)

if pattern:
  print(pattern.group(1))
