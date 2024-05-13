class Enrollment:
    def __init__(self, enrollment_id, student, course, enrollment_date):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date

    def get_enrollment_id(self):
        return self.enrollment_id

    def get_student_id(self):
        return self.student.get_student_id()

    def get_course_id(self):
        return self.course.get_course_id()

    def get_enrollment_date(self):
        return self.enrollment_date

    def get_student(self):
        return self.student

    def get_course(self):
        return self.course
