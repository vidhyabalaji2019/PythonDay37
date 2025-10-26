# Student Database Management System

# Empty dictionary to store student details
students = {}

# Function to add a student
def add_student(student_id, name, age, course):
    students[student_id] = {"name": name, "age": age, "course": course}
    print(f"Student {name} added successfully!")

# Function to update a student's details
def update_student(student_id, key, value):
    if student_id in students:
        students[student_id][key] = value
        print(f"Student {student_id} updated successfully!")
    else:
        print("Student not found!")

# Function to remove a student
def remove_student(student_id):
    if student_id in students:
        del students[student_id]
        print(f"Student {student_id} removed successfully!")
    else:
        print("Student not found!")

# Function to display all students
def display_students():
    if students:
        for student_id, details in students.items():
            print(f"ID: {student_id}, Name: {details['name']}, Age: {details['age']}, Course: {details['course']}")
    else:
        print("No students in the database.")

# Example Usage
add_student(101, "Alice", 20, "Computer Science")
add_student(102, "Bob", 21, "Mathematics")
update_student(101, "age", 21)
remove_student(102)
display_students()
