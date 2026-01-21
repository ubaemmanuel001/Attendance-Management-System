print("===== Attendance Management System =====")

# Ask for number of students
num_students = int(input("Enter number of students: "))

students = []
attendance = {}

# Input student names
for i in range(num_students):
    name = input(f"Enter name of student {i + 1}: ")
    students.append(name)

# Mark attendance
print("\nMark Attendance (P = Present, A = Absent)")
for student in students:
    status = input(f"{student}: ").upper()
    if status == "P":
        attendance[student] = "Present"
    else:
        attendance[student] = "Absent"

# Display attendance report
print("\n===== Attendance Report =====")
for student, status in attendance.items():
    print(student, "-", status)