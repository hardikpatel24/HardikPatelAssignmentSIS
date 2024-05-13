from datetime import datetime


class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.enrollments = ()
        self.payments = ()

    def get_student_id(self):
        return self.student_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_date_of_birth(self):
        return self.date_of_birth

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    def get_enrollments(self):
        return self.enrollments

    def get_payments(self):
        return self.payments

    def enroll_in_course(self, course):
        enrollment = Enrollment(len(self.enrollments) + 1, self, course, datetime.now())
        self.enrollments.append(enrollment)
        course.enrollments.append(enrollment)

    def update_student_info(self, first_name, last_name, date_of_birth, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number

    def make_payment(self, amount, payment_date):
        payment = Payment(len(self.payments) + 1, self, amount, payment_date)
        self.payments.append(payment)

    def display_student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")

    def get_enrolled_courses(self):
        return (enrollment.course for enrollment in self.enrollments)

    def get_payment_history(self):
        return self.payments
