from entity.model import Enrollment, Students, Courses, Teachers, Payments
from dao.db_interaction import DBInteraction
from util.db_conn_util import DBConnectivity

class SISServiceProvider:
    def __init__(self):
        self.db_conn_util = DBConnectivity()

    def add_enrollment(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.enrollment_id = int(input("Enter the enrollment id: "))
        self.student_id = int(input("Enter the student id: "))
        self.course_id = int(input("Enter the course id: "))
        self.enrollment_date = input("Enter the enrollment date: ")

        cursor.execute(
            "INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES (%s,%s,%s,%s)",
            (self.enrollment_id, self.student_id, self.course_id, self.enrollment_date))

        conn.commit()
        conn.close()

    def assign_teacher_to_course(self, teacher, course):
        course.assign_teacher(teacher)
        DBInteraction().update_course(course)

    def record_payment(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.student_id = int(input("Enter the student id: "))
        cursor.execute("SELECT * FROM Payments WHERE student_id = %s", (self.student_id,))
        rows = cursor.fetchall()
        for i in rows:
            print(i)
        conn.close()
        return None

    def generate_enrollment_report(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.course_id = int(input("Enter the course id: "))
        cursor.execute("SELECT * FROM Enrollments WHERE course_id = %s", (self.course_id,))
        rows = cursor.fetchall()

        for i in rows:
            print(i)

        conn.close()
        return None

    def generate_payment_report(self, student_id):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        sql = "SELECT amount from Payments where payment_id=?"
        payment_id = 11  # Example payment_id, replace it with actual value
        cursor.execute(sql, (payment_id,))
        row = cursor.fetchone()
        if row:
            amount = row[0]
            return amount
        else:
            return None

    def calculate_course_statistics(self):
        enrollments = DBInteraction().get_enrollments_for_course()
        total_enrollments = len(enrollments)
        total_payments = sum([enrollment.student.get_payment() for enrollment in enrollments])
        return total_enrollments, total_payments
