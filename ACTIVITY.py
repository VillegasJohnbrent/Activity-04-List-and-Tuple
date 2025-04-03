import pickle

# Sample data to start with
students = [
    (123456, ("John", "Doe"), "Sophomore", 85, 90),  # Student ID, Name, Class Standing, Major Exam Grade
    (654321, ("Jane", "Smith"), "Freshman", 75, 80),
]

def save_file(filename, data):
    """Save the student records to a file."""
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def load_file(filename):
    """Load student records from a file."""
    try:
        with open(filename, 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        print("File not found, starting with an empty record.")
        return []

def show_all_students():
    """Display all student records."""
    if not students:
        print("No student records available.")
        return
    for student in students:
        student_id, name, class_standing, major_exam_grade = student
        grade = 0.6 * class_standing + 0.4 * major_exam_grade
        print(f"ID: {student_id}, Name: {name[0]} {name[1]}, Class: {class_standing}, Major Exam Grade: {major_exam_grade}, Final Grade: {grade}")

def order_by_last_name():
    """Sort and display students by their last name."""
    sorted_students = sorted(students, key=lambda student: student[1][1])  # Sorting by last name
    for student in sorted_students:
        student_id, name, class_standing, major_exam_grade = student
        grade = 0.6 * class_standing + 0.4 * major_exam_grade
        print(f"ID: {student_id}, Name: {name[0]} {name[1]}, Class: {class_standing}, Major Exam Grade: {major_exam_grade}, Final Grade: {grade}")

def order_by_grade():
    """Sort and display students by their calculated grade."""
    sorted_students = sorted(students, key=lambda student: 0.6 * student[2] + 0.4 * student[3], reverse=True)  # Sorting by grade (60% class standing, 40% exam grade)
    for student in sorted_students:
        student_id, name, class_standing, major_exam_grade = student
        grade = 0.6 * class_standing + 0.4 * major_exam_grade
        print(f"ID: {student_id}, Name: {name[0]} {name[1]}, Class: {class_standing}, Major Exam Grade: {major_exam_grade}, Final Grade: {grade}")

def add_record():
    """Add a new student record."""
    student_id = int(input("Enter Student ID (6 digits): "))
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = int(input("Enter Class Standing (Grade): "))
    major_exam_grade = int(input("Enter Major Exam Grade: "))

    # Adding the record to the list
    students.append((student_id, (first_name, last_name), class_standing, major_exam_grade))
    print("Record added successfully.")

def edit_record():
    """Edit an existing student record."""
    student_id = int(input("Enter Student ID to edit: "))
    for idx, student in enumerate(students):
        if student[0] == student_id:
            first_name = input("Enter new First Name: ")
            last_name = input("Enter new Last Name: ")
            class_standing = int(input("Enter new Class Standing (Grade): "))
            major_exam_grade = int(input("Enter new Major Exam Grade: "))

            students[idx] = (student_id, (first_name, last_name), class_standing, major_exam_grade)
            print("Record updated successfully.")
            return
    print("Student ID not found.")

def delete_record():
    """Delete a student record."""
    student_id = int(input("Enter Student ID to delete: "))
    for idx, student in enumerate(students):
        if student[0] == student_id:
            del students[idx]
            print(f"Record with ID {student_id} deleted successfully.")
            return
    print("Student ID not found.")

def show_student_record():
    """Show details of a specific student by ID."""
    student_id = int(input("Enter Student ID to show: "))
    for student in students:
        if student[0] == student_id:
            first_name, last_name = student[1]
            class_standing = student[2]
            major_exam_grade = student[3]
            grade = 0.6 * class_standing + 0.4 * major_exam_grade
            print(f"ID: {student_id}, Name: {first_name} {last_name}, Class: {class_standing}, Major Exam Grade: {major_exam_grade}, Final Grade: {grade}")
            return
    print("Student ID not found.")

def main():
    """Main function to interact with the menu."""
    while True:
        print("\nStudent Record Management System")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            filename = input("Enter file name to open: ")
            global students
            students = load_file(filename)
        elif choice == '2':
            filename = input("Enter file name to save: ")
            save_file(filename, students)
        elif choice == '3':
            filename = input("Enter new file name to save as: ")
            save_file(filename, students)
        elif choice == '4':
            show_all_students()
        elif choice == '5':
            order_by_last_name()
        elif choice == '6':
            order_by_grade()
        elif choice == '7':
            show_student_record()
        elif choice == '8':
            add_record()
        elif choice == '9':
            edit_record()
        elif choice == '10':
            delete_record()
        elif choice == '11':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()