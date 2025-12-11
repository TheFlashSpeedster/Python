"""
Q5. Lambda Function

Create lambda to compute sum of digits of a number
"""

n = int(input())

sum_digits = lambda n: sum(int(digit) for digit in str(n))

print(sum_digits(n))