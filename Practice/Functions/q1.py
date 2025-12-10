"""
Q1. Function with Default Arguments
Write a function greet(name, msg="Welcome") that prints a greeting.
"""

def greet(name, msg="Welcome"):
  print(msg, name)

greet("Tony", "Hello")
greet("Tony")


"""
Q2. Function Returning Multiple Values
Write a function compute(n) that returns square and cube of n.
"""

def compute(n):
  sq = n**2
  cube = n**3
  print("Square:", sq)
  print("Cube:", cube)

compute(3)

"""
Q3. Function with *args
Write a function average(*nums) that returns the average of numbers.
"""

def average(*args):
  size = len(args) # no of numbers
  total = sum(args) # 
  avg = total/size
  print(avg)

average(2,3,10)

"""
Q4. Function with **kwargs
Write a function student_details(**info) that prints key-value pairs.
"""

def student_details(**info):
  for key, value in info.items():
    print(f"{key}: {info[key]}")


student_details(name="Tony", marks=34)

"""
Q5. Lambda Function
Create lambda to compute sum of digits of a number.
"""

num = "123"
total = lambda num: sum(int(digit) for digit in num)
print(total(num))

"""
Q6. Recursion
Write recursive function sum_digits(n).
"""

def sum_digits(n):
  if n == 0:
    return 0
  else:
    return (n % 10) + sum_digits(n // 10)

print(sum_digits(123))

"""
Q7. Nested Functions
Write outer function that returns factorial using inner function.
"""

def outer(n):
  def inner(n):
    f = 1
    for i in range(1, n + 1):
      f *= i
    return f
  return(inner(n))

print(outer(5))