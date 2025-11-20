n1 = int(input("First Number:"))
n2 = int(input("Second Number:"))

op = input("Enter Operator:")

match op:
    case "+":
        print("Sum is:", n1+n2)
    case "-":
        print("Difference is:", n1-n2)
    case "*":
        print("Product is:", n1*n2)
    case "/":
        print("Quotient is:", n1/n2)
    case "//":
        print("Floor Division Quotient is:", n1//n2)
    case _:
        print("Invalid Operator!")