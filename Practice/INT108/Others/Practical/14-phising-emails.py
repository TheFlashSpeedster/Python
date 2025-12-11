import re

with open("Practice/INT108/Others/Practical/sample14.txt", "r") as file:
  data = file.read()

pattern = r"[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}"
emails = re.findall(pattern, data)

count = dict()
for email in emails:
  if email in count:
    count[email] += 1
  else:
    count[email] = 1

most_common = max(count, key=count.get)
print(most_common)