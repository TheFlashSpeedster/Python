# Find Greatest Number

n1 = int(input("First Number:"))
n2 = int(input("Second Number:"))
n3 = int(input("Third Number:"))

if n1 > n2 and n1 > n3:
    print("Greatest Number:", n1)

elif n2 > n1 and n2 > n3:
    print("Greatest Number:", n2)

else:
    print("Greatest Number:", n3)