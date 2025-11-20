# Factorial of a number using function
## Factorial of n = n*(n-1)*(n-2)*....1
## OR Factorial = 1*2*3*...*n
## Range = (1, n+1)

def factorial(n):
  fac = 1
  for i in range(1, n+1):
    fac *= i
  return fac

n = int(input("Number: "))
print(factorial(n))