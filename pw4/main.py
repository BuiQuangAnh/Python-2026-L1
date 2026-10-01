import curses
import input as inp
import output as out

def main_app(stdscr):
    curses.curs_set(1)  
    
    students = []
    courses = []
    marks = {}

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "="*45, curses.A_BOLD)
        stdscr.addstr(1, 0, " STUDENT MARK MANAGEMENT ", curses.A_REVERSE)
        stdscr.addstr(2, 0, "="*45, curses.A_BOLD)
        stdscr.addstr(4, 2, "1. Input students")
        stdscr.addstr(5, 2, "2. Input courses")
        stdscr.addstr(6, 2, "3. Input marks")
        stdscr.addstr(7, 2, "4. List students")
        stdscr.addstr(8, 2, "5. List courses")
        stdscr.addstr(9, 2, "6. Show marks for a course")
        stdscr.addstr(10, 2, "7. Sort students by GPA descending")
        stdscr.addstr(11, 2, "0. Exit")
        stdscr.addstr(13, 2, "Select an option: ")
        
        stdscr.refresh()
        
        choice = stdscr.getch()
        
        if choice == ord('1'):
            inp.input_students(stdscr, students)
        elif choice == ord('2'):
            inp.input_courses(stdscr, courses)
        elif choice == ord('3'):
            inp.input_marks(stdscr, students, courses, marks)
        elif choice == ord('4'):
            out.list_students(stdscr, students)
        elif choice == ord('5'):
            out.list_courses(stdscr, courses)
        elif choice == ord('6'):
            out.show_marks(stdscr, students, marks)
        elif choice == ord('7'):
            out.sort_students_by_gpa(stdscr, students, marks, courses)
        elif choice == ord('0'):
            break
        else:
            stdscr.addstr(15, 2, "Invalid option. Press any key to try again.")
            stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main_app)