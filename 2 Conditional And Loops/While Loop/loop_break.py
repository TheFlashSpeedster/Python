# While Loop with BREAK
# break - ends loop on condition meet

# Example 1
x = 4
y = 0

while x >= 0:
    x -= 1
    y += 1
    if x == y:
        break # end loop
    else:
        print(x,y) # 3 1

# Example 2
x = 4
y = 0

while x >= 0:
    if x == y:
        break # end loop, when x = y = 2
    else:
        print(x,y) # prints: 4 0, 3 1
    x -= 1 # or x = x - 1
    y += 1 # or y = y + 1