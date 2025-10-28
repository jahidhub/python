marks = int(input("Enter Your marks: "))

if (marks <= 100) & (marks >= 90):
    grade = "EX"

elif (marks <= 90) & (marks >= 80):
    grade = "A"
elif (marks <= 80) & (marks >= 70):
    grade = "B"
elif (marks <= 70) & (marks >= 60):
    grade = "C"
elif (marks <= 60) & (marks >= 50):
    grade = "D"
elif marks <= 50:
    grade = "F"

print(f"Your garde is: {grade}")
