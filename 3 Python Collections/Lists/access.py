# Indexing
# L2R = 0 1 2 3 4 5
list = [10, 20, 30, 40, 50]

print(list[0]) # 10
print(list[1]) # 20
print(list[2]) # 30
print(list[3]) # 40
print(list[4]) # 50

# Negative Indexing
# R2L = -1 -2 -3 -4 -5

print(list[-1]) # 50
print(list[-2]) # 40
print(list[-3]) # 30
print(list[-4]) # 20
print(list[-5]) # 10

# Range of Indexes

print(list[0:5]) # prints all # index 0 to 3
print(list[0:1]) # prints 10 # index 0 only
print(list[2:4]) # prints 30 40 # index 2 to 3

print(list[-5:0]) # prints all
print(list[-5:-1]) # prints 10 20 30 40
print(list[-3:-1]) # prints 30 40
print(list[-5:-3]) # prints 10 20