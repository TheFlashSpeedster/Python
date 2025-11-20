# Find Greatest Number
# In Nested IF ELSE Style

n1 = int(input("First Number:"))
n2 = int(input("Second Number:"))
n3 = int(input("Third Number:"))

if n1 > n2:
    if n1 > n3:
        print("Greatest Number:", n1)
    else:
        print("Greatest Number:", n3)
else:
    if n2 > n3:
        print("Greatest Number:", n2)
    else:
        print("Greatest Number:", n3)