marks = int(input("\nEnter your marks: "))

grade = ""

if marks > 89 and marks < 101:
    grade = "A"
elif marks > 79:
    grade = "B"
elif marks > 69:
    grade = "C"
elif marks > 59:
    grade = "D"
else:
    grade = "F"

print(grade)
