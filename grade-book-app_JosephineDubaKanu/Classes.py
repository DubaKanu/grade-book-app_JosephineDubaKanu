class Student:
    def __init__(self, email, names):
        self.email = email
        self.names = names
        self.courses_registered = []
        self.GPA = 0.0

    def calculate_GPA(self):
        # Logic to calculate GPA based on courses and grades
        # Assuming a simple average for now
        total_credits = sum(course.credits for course in self.courses_registered)
        total_grade_points = sum(course.grade * course.credits for course in self.courses_registered)
        if total_credits > 0:
            self.GPA = total_grade_points / total_credits

    def register_for_course(self, course):
        self.courses_registered.append(course)

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)

    def register_student_for_course(self, student_email, course_name):
        # Find student and course
        # Add course to student's courses_registered list

    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()

    def calculate_ranking(self):
        # Sort students by GPA in descending order

    def search_by_grade(self, min_gpa, max_gpa):
        # Filter students based on GPA range

    def generate_transcript(self, student_email):
        # Find student and print transcript information
