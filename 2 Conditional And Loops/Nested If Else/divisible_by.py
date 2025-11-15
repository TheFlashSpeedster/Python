no = int(input("Enter Number:"))

if no % 15 == 0:
    print("Divisible by 15")
else:
    if no % 5 == 0 or no % 3 == 0:
        print("Divisible by 3 or 5 but not 15")
    else:
        print("Not Divisible by 3 or 5 or 15")
    