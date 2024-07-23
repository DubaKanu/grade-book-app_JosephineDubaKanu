from student import Student
from course import Course

class GradeBook:
    def __init__(self):
        self.student_list = {}
        self.course_list = {}

    def add_student(self, student):
        self.student_list[student.email] = student

    def add_course(self, course):
        self.course_list[course.name] = course

    def register_student_for_course(self, student_email, course_name):
        if student_email in self.student_list and course_name in self.course_list:
            self.student_list[student_email].register_for_course(course_name, self.course_list[course_name])

    def calculate_GPA(self, student_email):
        if student_email in self.student_list:
            self.student_list[student_email].calculate_GPA()

    def calculate_ranking(self):
        return sorted(self.student_list.values(), key=lambda s: s.GPA, reverse=True)

    def search_by_grade(self, grade):
        result = []
        for student in self.student_list.values():
            for course in student.courses_registered.values():
                if course['grade'] == grade:
                    result.append(student)
                    break
        return result

    def generate_transcript(self, student_email):
        if student_email in self.student_list:
            student = self.student_list[student_email]
            return f"Transcript for {student.names}\nGPA: {student.GPA}\nCourses: {student.courses_registered}"
