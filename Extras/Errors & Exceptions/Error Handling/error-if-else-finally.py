# Else Finally
try:
    num = int(input("Enter a number: "))
    result = num / 0
    # result = 10 / num # This will raise a ValueError if num is 0
    # ValueError if input is not an integer

except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
else: # This block executes if no exceptions were raised
    print(f"The result is: {result}")
finally: # This block will always execute
    print("Execution completed.")