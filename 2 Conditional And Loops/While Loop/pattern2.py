# rows = n, columns = n, to print = 1 to n

n = int(input("Enter N:"))

for i in range(n): # loop for rows
    for j in range(1,n+1): # loop for columns
        print(j, end="")
    print()