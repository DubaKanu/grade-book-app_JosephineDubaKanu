from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = {}
        self.course_list = {}

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list[email] = student

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list[name] = course

    def register_student_for_course(self, student_email, course_name, grade):
        if student_email in self.student_list and course_name in self.course_list:
            course = self.course_list[course_name]
            course_info = {"course": course, "credits": course.credits, "grade": grade}
            self.student_list[student_email].register_for_course(course_name, course_info)

    def calculate_GPA(self, student_email):
        if student_email in self.student_list:
            self.student_list[student_email].calculate_GPA()

    def calculate_ranking(self):
        return sorted(self.student_list.values(), key=lambda s: s.GPA, reverse=True)

    def search_by_grade(self, min_grade, max_grade):
        result = []
        for student in self.student_list.values():
            if min_grade <= student.GPA <= max_grade:
                result.append(student)
        return result

    def generate_transcript(self, student_email):
        if student_email in self.student_list:
            student = self.student_list[student_email]
            transcript = f"Transcript for {student.names}\nGPA: {student.GPA}\nCourses:\n"
            for course_name, course_info in student.courses_registered.items():
                transcript += f"- {course_name}: Grade {course_info['grade']}\n"
            return transcript
