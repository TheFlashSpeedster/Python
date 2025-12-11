"""
3.Write a Program to check if the entered number is Armstrong or not.
"""

# Armstrong number - (sum of digits)^ (number of digits) == number

n = int(input("Enter Number: "))

s = str(n)
power = len(str(n))
sum_digits = 0

for digit in s:
  sum_digits += int(digit)**power

if sum_digits == n:
  print("Armstrong")
else:
  print("Not Armstrong")