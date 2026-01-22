from datetime import datetime

print("===== Attendance Management System =====")

attendance_records = {}

def take_attendance():
    date = datetime.now().strftime("%Y-%m-%d")
    print("\nTaking attendance for date:", date)

    num_students = int(input("Enter number of students: "))

    for i in range(num_students):
        student_id = input("\nEnter Student ID: ")
        student_name = input("Enter Student Name: ")

        status = input("Mark Attendance (P/A): ").upper()
        if status == "P":
            status = "Present"
        else:
            status = "Absent"

        if student_id not in attendance_records:
            attendance_records[student_id] = {
                "name": student_name,
                "records": {}
            }

        attendance_records[student_id]["records"][date] = status

    print("\nAttendance recorded successfully.")


def view_all_attendance():
    if not attendance_records:
        print("\nNo attendance records available.")
        return

    print("\n===== All Attendance Records =====")
    for student_id, details in attendance_records.items():
        print("\nStudent ID:", student_id)
        print("Name:", details["name"])
        for date, status in details["records"].items():
            print(date, "-", status)


def search_by_student_id():
    student_id = input("\nEnter Student ID to search: ")

    if student_id not in attendance_records:
        print("Student not found.")
        return

    student = attendance_records[student_id]
    print("\nStudent Name:", student["name"])
    for date, status in student["records"].items():
        print(date, "-", status)


def attendance_percentage():
    student_id = input("\nEnter Student ID: ")

    if student_id not in attendance_records:
        print("Student not found.")
        return

    records = attendance_records[student_id]["records"]
    total_days = len(records)
    present_days = sum(1 for status in records.values() if status == "Present")

    percentage = (present_days / total_days) * 100 if total_days > 0 else 0

    print("\nAttendance Percentage:")
    print(attendance_records[student_id]["name"], "-", round(percentage, 2), "%")


def save_to_file():
    with open("attendance_records.txt", "w") as file:
        for student_id, details in attendance_records.items():
            file.write(f"Student ID: {student_id}\n")
            file.write(f"Name: {details['name']}\n")
            for date, status in details["records"].items():
                file.write(f"{date} - {status}\n")
            file.write("\n")

    print("\nAttendance records saved to attendance_records.txt")


while True:
    print("\n===== MENU =====")
    print("1. Take Attendance")
    print("2. View All Attendance")
    print("3. Search Attendance by Student ID")
    print("4. Calculate Attendance Percentage")
    print("5. Save Attendance to File")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        take_attendance()
    elif choice == "2":
        view_all_attendance()
    elif choice == "3":
        search_by_student_id()
    elif choice == "4":
        attendance_percentage()
    elif choice == "5":
        save_to_file()
    elif choice == "6":
        print("\nExiting system...")
        break
    else:
        print("\nInvalid choice. Try again.")
