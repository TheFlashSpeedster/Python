"""
Q3. Grade of Student (Medium) 
Input marks (0–100) and print grade: 
90–100: A, 80–89: B, 70–79: C, 60–69: D, else: F.
"""

marks = int(input())

if marks>=90:
  print("A")
elif marks>=80:
  print("B")
elif marks>=70:
  print("C")
elif marks>=60:
  print("D")
else:
  print("F")