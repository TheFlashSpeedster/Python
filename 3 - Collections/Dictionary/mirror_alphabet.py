'''
Given a string and a number N, we need to mirror the characters
from the N-th position up to the length of the string in
alphabetical order. In mirror operation, we change 'a' to 'z', 'b' to
'y', and so on.

Input : N = 3
paradox
Output : paizwlc

Input : N = 6
pneumonia
Output : pneumlmrz
'''
# Mirror Table

# a b c d e f g h i j k l m
# z y x w v u t s r q p o n

# paradox at N = 3 == paIZWLC
# pneumonia at N = 6 == pneumLMRZ

alpha = "abcdefghijklmnopqrstuvwxyz" # original letters
rev_alpha = alpha[::-1] # mirror letters

# dict [original letter (key) & mirror letters (value)]
dict1 = dict(zip(alpha, rev_alpha)) 

main_str = input("Enter String: ")
n = int(input("Enter Element Position:"))

prefix = main_str[:n-1] # first part
suffix = main_str[n-1:] # second part

mirror = '' # to store mirrored string

for i in range(len(suffix)):
  mirror = mirror + dict1[suffix[i]]

# final string
final_str = prefix + mirror
print(final_str)