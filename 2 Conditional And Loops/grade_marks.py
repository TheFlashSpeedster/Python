# Take input percentage of a student and print the Grade according to marks:

marks = int(input("Enter Marks:"))

if marks>80:
    print("Very Good")
elif marks>60:
    print("Good")
elif marks>40:
    print("Average")
else:
    print("Fail")