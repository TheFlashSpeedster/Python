# eng and maths both above 80 = A Grade
# if any (eng or maths) above 80 = B Grade
# eng and maths both below 80 = C Grade

eng_marks = int(input("Enter English Marks:"))
math_marks = int(input("Enter Mathematics Marks:"))

if eng_marks > 80 and math_marks > 80:
    print("Grade: A")
elif eng_marks > 80 or math_marks > 80:
    print("Grade: B")
else:
    print("Grade: C")