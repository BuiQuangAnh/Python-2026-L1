import curses
import math
from domains.models import Student, Course

def get_string(stdscr, y, x, prompt):
    """String input."""
    stdscr.addstr(y, x, prompt)
    curses.echo()
    result = stdscr.getstr(y, x + len(prompt), 50).decode('utf-8')
    curses.noecho()
    return result

def input_students(stdscr, students_list):
    stdscr.clear()
    try:
        num = int(get_string(stdscr, 0, 0, "Enter number of students: "))
        for i in range(num):
            stdscr.clear()
            stdscr.addstr(0, 0, f"Entering Details for Student {i+1}", curses.A_BOLD)
            s_id = get_string(stdscr, 2, 0, "Student ID: ")
            name = get_string(stdscr, 3, 0, "Student Name: ")
            dob = get_string(stdscr, 4, 0, "Date of Birth (DD/MM/YYYY): ")
            students_list.append(Student(s_id, name, dob))
        stdscr.addstr(6, 0, "Students added successfully! Press any key to continue.")
    except ValueError:
        stdscr.addstr(2, 0, "Invalid input. Press any key to return.")
    stdscr.getch()

def input_courses(stdscr, courses_list):
    stdscr.clear()
    try:
        num = int(get_string(stdscr, 0, 0, "Enter number of courses: "))
        for i in range(num):
            stdscr.clear()
            stdscr.addstr(0, 0, f"Entering Details for Course {i+1}", curses.A_BOLD)
            c_id = get_string(stdscr, 2, 0, "Course ID: ")
            name = get_string(stdscr, 3, 0, "Course Name: ")
            credit = int(get_string(stdscr, 4, 0, "Course Credits (e.g., 3): "))
            courses_list.append(Course(c_id, name, credit))
        stdscr.addstr(6, 0, "Courses added successfully! Press any key to continue.")
    except ValueError:
        stdscr.addstr(2, 0, "Invalid input. Press any key to return.")
    stdscr.getch()

def input_marks(stdscr, students_list, courses_list, marks_dict):
    stdscr.clear()
    if not courses_list or not students_list:
        stdscr.addstr(0, 0, "Please add students and courses first. Press any key.")
        stdscr.getch()
        return

    course_id = get_string(stdscr, 0, 0, "Enter Course ID to input marks: ")
    if course_id not in [c.id for c in courses_list]:
        stdscr.addstr(2, 0, "Course ID not found! Press any key.")
        stdscr.getch()
        return
        
    if course_id not in marks_dict:
        marks_dict[course_id] = {}
        
    stdscr.clear()
    stdscr.addstr(0, 0, f"Entering Marks for Course: {course_id}", curses.A_BOLD)
    
    row = 2
    for student in students_list:
        try:
            raw_mark = float(get_string(stdscr, row, 0, f"Enter mark for {student.name} (0-20): "))
            floored_mark = math.floor(raw_mark * 10) / 10.0
            marks_dict[course_id][student.id] = floored_mark
        except ValueError:
            stdscr.addstr(row + 1, 0, "Invalid mark, saving as 0.0")
            marks_dict[course_id][student.id] = 0.0
        row += 2
        
    stdscr.addstr(row + 1, 0, "Marks added successfully! Press any key.")
    stdscr.getch()