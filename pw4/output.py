import curses
import numpy as np

def list_students(stdscr, students_list):
    stdscr.clear()
    stdscr.addstr(0, 0, "List of Students", curses.A_BOLD)
    row = 2
    for student in students_list:
        stdscr.addstr(row, 0, f"ID: {student.id} | Name: {student.name} | DoB: {student.dob}")
        row += 1
    stdscr.addstr(row + 2, 0, "Press any key to return...")
    stdscr.getch()

def list_courses(stdscr, courses_list):
    stdscr.clear()
    stdscr.addstr(0, 0, "List of Courses", curses.A_BOLD)
    row = 2
    for course in courses_list:
        stdscr.addstr(row, 0, f"ID: {course.id} | Name: {course.name} | Credits: {course.credits}")
        row += 1
    stdscr.addstr(row + 2, 0, "Press any key to return...")
    stdscr.getch()

def show_marks(stdscr, students_list, marks_dict):
    stdscr.clear()
    curses.echo()
    stdscr.addstr(0, 0, "Enter Course ID to view marks: ")
    course_id = stdscr.getstr(0, 31, 20).decode('utf-8')
    curses.noecho()
    
    stdscr.clear()
    if course_id in marks_dict:
        stdscr.addstr(0, 0, f"Marks for Course {course_id}", curses.A_BOLD)
        row = 2
        for student in students_list:
            m = marks_dict[course_id].get(student.id, "No mark")
            stdscr.addstr(row, 0, f"{student.name}: {m}")
            row += 1
    else:
        stdscr.addstr(0, 0, "No marks found for this course.")
        
    stdscr.addstr(curses.LINES - 2, 0, "Press any key to return...")
    stdscr.getch()

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

def sort_students_by_gpa(stdscr, students_list, marks_dict, courses_list):
    stdscr.clear()
    student_gpas = []
    for student in students_list:
        gpa = calculate_gpa(student, marks_dict, courses_list)
        student_gpas.append((student, gpa))
        
    student_gpas.sort(key=lambda x: x[1], reverse=True)
    
    stdscr.addstr(0, 0, "Students Sorted by GPA (Descending)", curses.A_BOLD)
    row = 2
    for student, gpa in student_gpas:
        stdscr.addstr(row, 0, f"Name: {student.name} (ID: {student.id}) - GPA: {gpa:.2f}")
        row += 1
        
    stdscr.addstr(row + 2, 0, "Press any key to return...")
    stdscr.getch()