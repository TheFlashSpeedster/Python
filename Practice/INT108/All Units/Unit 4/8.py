"""
Q8. Dictionary Word Count (Medium–High) 
Count occurrences of each word in a sentence and store in dictionary.
"""

sentence = input().split() # list of words
freq = {} # empty dict

for word in sentence:
  if word in freq:
    freq[word] += 1 # increase count in next occurences
  else:
    freq[word] = 1 # set count 1 (if first occurence)

print(freq)