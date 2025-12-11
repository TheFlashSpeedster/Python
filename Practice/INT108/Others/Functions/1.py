"""
Q1. Function with Default Arguments

Write a function greet(name, msg="Welcome") that prints a greeting.
"""

def greet(name, msg="Welcome"):
  print(f"{msg}, {name}")

greet("Tony")
greet("David", "Bye")