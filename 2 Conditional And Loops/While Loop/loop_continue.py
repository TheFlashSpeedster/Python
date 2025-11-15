# while loop with continue
# continue - skip line

x = 4
y = 0

while x >= 0:
    x -= 1
    y += 1
    if x == y:
        continue # jumps back to while
    else:
        print(x,y) # 3 1, 1 3, 0 4, -1 5