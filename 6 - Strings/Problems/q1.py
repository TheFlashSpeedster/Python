"""
Consider a string: 'The unexpected always happens".

1. Assign this string to a variable: text.
2. Print the string.
3. Print the length of the string.
4. Check if the phrase 'pp' is present in the string.
5. Print the substring from O till l0th index.
6. Replace 'always' with 'never.
7. Add "no matter what" to the string.
8. Print the final string.
"""

text = "The unexpected always happens "
print(text)
print(len(text))
print("\"pp\" is present: ", True if text.find("pp")!=-1 else False)
print(text[0:10])
print(text.replace("always", "never"))
text_extra = "no matter what"
print(text+text_extra)