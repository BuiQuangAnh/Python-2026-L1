import numpy as np
import curses

def list_courses(courses_list):
    print("\n--- Courses ---")
    for course in courses_list:
        print(f"ID: {course.id} | Name: {course.name} | Credits: {course.credits}")

def list_students(students_list):
    print("\n--- Students ---")
    for student in students_list:
        print(f"ID: {student.id} | Name: {student.name} | DoB: {student.dob}")

def show_marks(students_list, marks_dict):
    course_id = input("Enter Course ID to view marks: ")
    if course_id in marks_dict:
        print(f"\n--- Marks for Course {course_id} ---")
        for student in students_list:
            m = marks_dict[course_id].get(student.id, "No mark")
            print(f"{student.name}: {m}")
    else:
        print("No marks found for this course.")

def calculate_gpa(student, marks_dict, courses_list):
    student_marks = []
    course_credits = []
    
    for course in courses_list:
        if course.id in marks_dict and student.id in marks_dict[course.id]:
            student_marks.append(marks_dict[course.id][student.id])
            course_credits.append(course.credits)
            
    if not student_marks:
        return 0.0
        
    marks_arr = np.array(student_marks)
    credits_arr = np.array(course_credits)
    total_credits = np.sum(credits_arr)
    
    if total_credits == 0:
        return 0.0
        
    gpa = np.sum(marks_arr * credits_arr) / total_credits
    return float(gpa)

def sort_students_by_gpa(students_list, marks_dict, courses_list):
    student_gpas = []
    for student in students_list:
        gpa = calculate_gpa(student, marks_dict, courses_list)
        student_gpas.append((student, gpa))
        
    student_gpas.sort(key=lambda x: x[1], reverse=True)
    
    print("\n--- Students Sorted by GPA (Descending) ---")
    for student, gpa in student_gpas:
        print(f"Name: {student.name} (ID: {student.id}) - GPA: {gpa:.2f}")

def curses_menu(stdscr):
    """Optional curses UI implementation"""
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr(0, 0, "=== STUDENT MARK MANAGEMENT (CURSES UI) ===", curses.A_BOLD)
    stdscr.addstr(2, 2, "Press any key to exit curses and return to CLI...")
    stdscr.refresh()
    stdscr.getch()