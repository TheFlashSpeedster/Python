# Datatypes

a = "This is test"
print(type(a))

b = 5
print(type(b))

c = 7.39
print(type(c))

d = True
print(type(d))

# Typecasting - Conversion of Datatypes

x = 5
y = 4
z = 11

x_str = str(x)
y_str = str(y)
z_str = str(z)

final_str = x_str + y_str + z_str
final_int = int(x_str + y_str + z_str)

print("Final String:", final_str, type(final_str))
print("Final Integer:", final_int, type(final_int))