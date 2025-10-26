# Student Attendance Management System

# Initialize an empty set for attendance
attendance = set()

# Function to mark attendance
def mark_attendance(name):
    attendance.add(name)
    print(f"{name} marked as present.")

# Function to remove a student (mark as absent)
def remove_student(name):
    if name in attendance:
        attendance.remove(name)
        print(f"{name} marked as absent.")
    else:
        print(f"{name} is not in the attendance list.")

# Function to display attendance
def display_attendance():
    if attendance:
        print("\n📌 Students Present Today:")
        for student in attendance:
            print(f"- {student}")
    else:
        print("\n❌ No students present.")

# Sample Execution
mark_attendance("Alice")
mark_attendance("Bob")
mark_attendance("Charlie")
display_attendance()
remove_student("Bob")
display_attendance()
