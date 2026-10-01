import math
from domains.models import Student, Course

def input_students(students_list):
    num = int(input("Enter number of students: "))
    for i in range(num):
        print(f"\n--- Student {i+1} ---")
        s_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("Date of Birth: ")
        students_list.append(Student(s_id, name, dob))

def input_courses(courses_list):
    num = int(input("Enter number of courses: "))
    for i in range(num):
        print(f"\n--- Course {i+1} ---")
        c_id = input("Course ID: ")
        name = input("Course Name: ")
        credit = int(input("Course Credits (e.g., 3): "))
        courses_list.append(Course(c_id, name, credit))

def input_marks(students_list, courses_list, marks_dict):
    course_id = input("Enter Course ID to input marks: ")
    if course_id not in [c.id for c in courses_list]:
        print("Course ID not found!")
        return
        
    if course_id not in marks_dict:
        marks_dict[course_id] = {}
        
    print(f"--- Entering Marks for Course: {course_id} ---")
    for student in students_list:
        raw_mark = float(input(f"Enter mark for {student.name} (0-20): "))
        floored_mark = math.floor(raw_mark * 10) / 10.0
        marks_dict[course_id][student.id] = floored_mark