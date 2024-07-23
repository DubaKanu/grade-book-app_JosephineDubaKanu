from gradebook import GradeBook

def main():
    gradebook = GradeBook()

    while True:
        print("Please select an action:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            gradebook.add_student(email, names)

        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            gradebook.add_course(name, trimester, credits)

        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade for the course: "))
            gradebook.register_student_for_course(student_email, course_name, grade)

        elif choice == '4':
            student_email = input("Enter student email: ")
            gradebook.calculate_GPA(student_email)

        elif choice == '5':
            ranking = gradebook.calculate_ranking()
            print("Student Ranking:")
            for student in ranking:
                print(f"{student.names}: GPA {student.GPA}")

        elif choice == '6':
            min_grade = float(input("Enter minimum grade: "))
            max_grade = float(input("Enter maximum grade: "))
            students = gradebook.search_by_grade(min_grade, max_grade)
            print("Search results:")
            for student in students:
                print(f">> {student.names} (GPA: {student.GPA})")

        elif choice == '7':
            student_email = input("Enter student email: ")
            transcript = gradebook.generate_transcript(student_email)
            print(transcript)

        elif choice == '8':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
