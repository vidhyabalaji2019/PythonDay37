# Student Course Enrollment System

# Set of available courses
available_courses = {"Mathematics", "Physics", "Chemistry", "Computer Science", "Biology"}

# Set to store courses a student enrolls in
student_courses = set()

# Function to enroll in a course
def enroll_course(course_name):
    if course_name in available_courses:
        student_courses.add(course_name)
        print(f"Enrolled in {course_name} successfully!")
    else:
        print("Course not found!")

# Function to remove a course
def drop_course(course_name):
    if course_name in student_courses:
        student_courses.remove(course_name)
        print(f"Dropped {course_name} successfully!")
    else:
        print(f"{course_name} is not in your enrolled courses.")

# Function to display enrolled courses
def show_enrolled_courses():
    if student_courses:
        print("\n📋 Enrolled Courses:")
        for course in student_courses:
            print(f"- {course}")
    else:
        print("No courses enrolled yet.")

# ------------------- Example Usage -------------------
enroll_course("Mathematics")
enroll_course("Computer Science")
enroll_course("History")  # Not available
enroll_course("Physics")

drop_course("Mathematics")
drop_course("Biology")    # Not enrolled

show_enrolled_courses()
