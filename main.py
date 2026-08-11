from student import Student
from calculator import calculate_total, calculate_percentage
from grade import calculate_grade


print("===== STUDENT GRADE CALCULATOR =====")

name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))

    while mark < 0 or mark > 100:
        print("Please enter marks between 0 and 100.")
        mark = float(input(f"Enter marks for Subject {i}: "))

    marks.append(mark)


# Create Student object
student = Student(name, marks)

# Calculate result
total = calculate_total(marks)
percentage = calculate_percentage(total)
grade = calculate_grade(percentage)


# Display result
print("\n===== STUDENT RESULT =====")

student.display_student()

print("Total Marks :", total, "/ 500")
print("Percentage   :", percentage, "%")
print("Grade        :", grade)