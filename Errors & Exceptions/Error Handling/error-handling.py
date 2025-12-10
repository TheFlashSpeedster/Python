# Error Handling in Python
# Error handling is an essential part of programming that allows you to manage and respond to errors

# Example:

try:
  st = int("Hello")
  n2 = 0
  print(n2)
  print(st)

except ZeroDivisionError:
  print("ZeroDivisionError")

except NameError:
  print("NameError")

except SyntaxError:
  print("SyntaxError")

except ValueError:
  print("ValueError")

except:
  print("Other Error")