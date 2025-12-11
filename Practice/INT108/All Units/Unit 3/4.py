"""
Q4. Use of math Module (Medium) 
Write function that takes radius and returns area and circumference.
"""
import math

def circle(r):
  area = math.pi * r ** 2
  circumference = 2 * math.pi * r
  return area, circumference

r = int(input("Radius: "))
a, c = circle(r)
print(f"Area: {a}")
print(f"Circumference: {c}")