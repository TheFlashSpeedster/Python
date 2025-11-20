# Recursion
## Technique where a function calls itself
## Involves a base case (termination condition) to terminate the recursion and a recursive case (function calls itself) that breaks the problem down into smaller subproblems.

def factorial(n):
  # base case (termination)
  if n==0:
    return 1
  
  # recursive case
  result = n * factorial(n-1)
  return result

# Print Value
print(factorial(5))