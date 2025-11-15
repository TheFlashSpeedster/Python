# Print the given pattern

# ***1    - i = 1
# **123   - i = 2
# *12345  - i = 3
# 1234567 - i = 4

# no of rows: n
# no of spaces in columns: n - i
# print: 2i - 1

n = int(input("Enter N:")) # loop for rows

for i in range(1, n+1): # i = 1 as start (cuz row)
    # printing spaces
    print(" " * (n-i), end="")

    # printing digits
    for j in range(1, 2 * i): # range(1, 2 * i - 1 + 1)
        print(j, end="")
    print()