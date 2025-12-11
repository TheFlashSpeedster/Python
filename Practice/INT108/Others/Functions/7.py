"""
Q7. Nested Functions
Write outer function that returns factorial using inner function.
"""

def outer(n):
  def inner():
    f = 1
    for i in range(1, n+1):
      f *= i
    return f
  return inner()

print(outer(5))