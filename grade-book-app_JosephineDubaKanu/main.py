def main():
    grade_book = GradeBook()
    while True:
        print("1. Add student")
        print("2. Add course")
        print("3. Register student for course")
        print("4. Calculate GPA")
        print("5. Calculate ranking")
        print("6. Search by grade")
        print("7. Generate transcript")
        print("8. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            # Add student logic
        elif choice == "2":
            # Add course logic
        # ... and so on

if __name__ == "__main__":
    main()
