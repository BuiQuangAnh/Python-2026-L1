import input as inp
import output as out
import curses

def main():
    students = []
    courses = []
    marks = {} 

    while True:
        print("\n" + "="*40)
        print("STUDENT MARK MANAGEMENT - MODULAR (PW4)")
        print("="*40)
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks for a course")
        print("7. Sort students by GPA descending")
        print("8. Test Curses UI")
        print("0. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            inp.input_students(students)
        elif choice == '2':
            inp.input_courses(courses)
        elif choice == '3':
            inp.input_marks(students, courses, marks)
        elif choice == '4':
            out.list_students(students)
        elif choice == '5':
            out.list_courses(courses)
        elif choice == '6':
            out.show_marks(students, marks)
        elif choice == '7':
            out.sort_students_by_gpa(students, marks, courses)
        elif choice == '8':
            curses.wrapper(out.curses_menu)
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()