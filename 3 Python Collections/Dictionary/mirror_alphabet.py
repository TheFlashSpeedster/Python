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

dict_alpha = dict(zip(alpha, rev_alpha)) # dict (original & mirror letters)

n = int(input("Enter Element Position:"))
strx = input("Enter String: ")

str1 = strx[:n-1] # first part
str2 = strx[n-1:] # second part
print(str1, str2)