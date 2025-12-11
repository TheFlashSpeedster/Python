"""
Q4. Function with **kwargs

Write a function student_details(**info) that prints key-value pairs.
"""

def student_details(**info):
  print(dict(info.items()))

student_details(name="Tony", marks=88, grade="B")
student_details(name="David", last="Das")