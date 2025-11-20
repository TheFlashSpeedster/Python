# Calculate 'a' raised to power 'b'

def power(a, b):
  if b==0:
    return 1
  
  result = a * power(a, b-1)
  return result

a = int(input("Number: "))
b = int(input("Power: "))

print(power(a,b))