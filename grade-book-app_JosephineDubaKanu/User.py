def main():
    gradebook = GradeBook()

    while True:
        print("Choose an action:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA")
        print("5. Calculate Ranking")
        print("6. Search by Grade")
        print("7. Generate Transcript")
        print("8. Exit")

        choice = input()

        if choice == '1':
            email = input("Enter student email: ")
            names = input("Enter student names: ")
            student = Student(email, names)
            gradebook.add_student(student)

        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            course = Course(name, trimester, credits)
            gradebook.add_course(course)

        elif choice == '3':
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            gradebook.register_student_for_course(student_email, course_name)

        elif choice == '4':
            student_email = input("Enter student email: ")
            gradebook.calculate_GPA(student_email)

        elif choice == '5':
            ranking = gradebook.calculate_ranking()
            for student in ranking:
                print(f"{student.names}: {student.GPA}")

        elif choice == '6':
            grade = float(input("Enter grade to search: "))
            students = gradebook.search_by_grade(grade)
            for student in students:
                print(student.names)

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
