# Arguments

## Positional Arguments
## Arguments are passed to functions in the order they are defined.

def greet(person):
  print("Hello", person)

greet("Rohan") # Hello Rohan
greet("Rahul") # Hello Rahul

## Keyword Arguments
## Arguments are passed to functions by explicitly naming each parameter and its corresponding value.

def sum(msg, name):
  output = f"{msg} {name}!"
  print(output)

x = "Rohan"
y = "Hello"

sum(name=x, msg=y) # Hello Rohan!
sum(name=y, msg=y) # Hello Hello!
sum(name=y, msg=x) # Rohan Hello!

## Default Arguments
## Default values are assigned to parameters in the function definition. If no argument is provided during the function call, the default value is used.

def greet(person="Guest"):
  print(f"Hello {person}")

# Value Provided
greet("Rohan") # Hello Rohan

# Value Not Provided
greet() # Hello Guest

## Variable-length Arguments

## Positional Args (Using *args)

def addNumbers(*args): # *anything can be used instead of *args
  sum = 0
  for i in args: # Loops through all arguments
    sum += i
  return sum

print(addNumbers(2,3)) # 5
print(addNumbers(4,10,15,20)) # 49
print(addNumbers(1,2,3,4,5,6,7,8,9,10)) # 55

## Keywords Args (Using **kwargs)
def studentInfo(**kwargs): # **anything can be used instead of **kwargs
  print(dict(kwargs.items()))

  for x, y in kwargs.items(): # (key, value) for each tuple
    print(f"{x} is {y}") # key is value

studentInfo(name="Rohan", age=10)
studentInfo(name="Rahul", place="Delhi")
studentInfo(name="Rohit", place="Delhi", age=12)