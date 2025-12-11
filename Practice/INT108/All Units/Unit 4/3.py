"""
Q3. Find Substring (Medium) 
Input string and substring; print first index if found, else -1 (without using find).
"""

main = input()
sub = input()

position = -1
for i in range(len(main) - len(sub) + 1):
  if main[i:i+len(sub)] == sub:
    position = i
    break

print("Position: ", position)