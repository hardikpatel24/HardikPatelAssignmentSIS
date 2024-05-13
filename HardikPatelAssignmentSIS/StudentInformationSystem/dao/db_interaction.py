from entity.model import Students, Courses, Teachers, Enrollment, Payments
from util.db_conn_util import DBConnectivity


class DBInteraction:
    def __init__(self):
        self.db_conn_util = DBConnectivity()

    def create_student(self):
        conn = self.db_conn_util.makeconnection()
        if conn is None:
            print("no connection")
        cursor = conn.cursor()
        self.student_id = int(input("Enter student id: "))
        self.first_name = input("Enter student first name: ")
        self.last_name = input("Enter student last name: ")
        self.date_of_birth = input("Enter student date of birth: ")
        self.email = input("Enter student email id: ")
        self.phone_number = input("Enter student phone number: ")
        cursor.execute(
            "INSERT INTO Students (student_id, first_name, last_name, date_of_birth, email, phone_number) VALUES (%s,%s,%s,%s,%s,%s)",
            (self.student_id, self.first_name, self.last_name, self.date_of_birth, self.email, self.phone_number))
        print("Student has been created successfully")

        conn.commit()
        conn.close()

    def create_course(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.course_id = int(input("Enter the course id: "))
        self.course_name = input("Enter the course name: ")
        self.course_code = input("Enter the course code: ")
        self.instructor_name = input("Enter the instructor name: ")

        cursor.execute(
            "INSERT INTO Courses (course_id, course_name, course_code, instructor_name) VALUES (%s,%s,%s,%s)",
            (self.course_id, self.course_name, self.course_code, self.instructor_name))
        print("Course has been created successfully")

        conn.commit()
        conn.close()

    def create_enrollment(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.enrollment_id = int(input("Enter the enrollment id: "))
        self.student_id = int(input("Enter the student id: "))
        self.course_id = int(input("Enter the course id: "))
        self.enrollment_date = input("Enter the enrollment date: ")

        cursor.execute(
            "INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES (%s,%s,%s,%s)",
            (self.enrollment_id, self.student_id, self.course_id, self.enrollment_date))
        print("Enrollment has been created successfully")

        conn.commit()
        conn.close()

    def create_teacher(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.teacher_id = int(input("Enter the teacher id: "))
        self.first_name = input("Enter teacher first name: ")
        self.last_name = input("Enter teacher last name: ")
        self.email = input("Enter the email id: ")

        cursor.execute("INSERT INTO Teachers (teacher_id, first_name, last_name, email) VALUES (%s,%s,%s,%s)",
                       (self.teacher_id, self.first_name, self.last_name, self.email))
        print("Teacher has been created successfully")

        conn.commit()
        conn.close()

    def create_payment(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.payment_id = int(input("Enter the payment id: "))
        self.student_id = int(input("Enter the student id: "))
        self.amount = int(input("Enter the amount: "))
        self.payment_date = input("Enter the payment date: ")

        cursor.execute("INSERT INTO Payments (payment_id, student_id, amount, payment_date) VALUES (%s,%s,%s,%s)",
                       (self.payment_id, self.student_id, self.amount, self.payment_date))
        print("Payment has been created successfully")

        conn.commit()
        conn.close()

    def get_student_by_id(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.student_id = int(input("Enter the student id: "))

        cursor.execute("SELECT * FROM Students WHERE student_id = %s", (self.student_id,))
        row = cursor.fetchall()
        for i in row:
            print(i)
        else:
            conn.close()
            return None

    def get_course_by_id(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.course_id = int(input("Enter the course id: "))

        cursor.execute("SELECT * FROM Courses WHERE course_id = %s", (self.course_id,))
        row = cursor.fetchone()

        for i in row:
            print(i)
        else:
            conn.close()
            return None

    def get_enrollments_for_student(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.student_id = int(input("Enter the student id: "))

        cursor.execute("SELECT * FROM Enrollments WHERE student_id = %s", (self.student_id,))
        rows = cursor.fetchall()

        for i in rows:
            print(i)

        conn.close()
        return None

    def get_enrollments_for_course(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.course_id = int(input("Enter the course id: "))
        cursor.execute("SELECT * FROM Enrollments WHERE course_id = %s", (self.course_id,))
        rows = cursor.fetchall()

        for i in rows:
            print(i)

        conn.close()
        return None

    def get_payments_for_student(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.student_id = int(input("Enter the student id: "))
        cursor.execute("SELECT * FROM Payments WHERE student_id = %s", (self.student_id,))
        rows = cursor.fetchall()

        for i in rows:
            print(i)

        conn.close()
        return payments

    def get_teacher_by_id(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.teacher_id = int(input("Enter the teacher id: "))
        cursor.execute("SELECT * FROM Teachers WHERE teacher_id = %s", (self.teacher_id,))
        row = cursor.fetchone()

        for i in row:
            print(i)
        else:
            conn.close()
            return None

    def update_student(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.student_id_id = int(input("Enter teacher id to update: "))
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.email = input("Enter email: ")
        self.phone_number = int(input("Enter the phone number of the student: "))

        cursor.execute(
            "UPDATE Students SET first_name = %s, last_name = %s, date_of_birth = %s, email = %s, phone_number = %s WHERE student_id = %s",
            (self.first_name, self.last_name, self.date_of_birth, self.email, self.phone_number, self.student_id))
        print("Student information has been updated successfully")

        conn.commit()
        conn.close()

    def update_course(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.course_name = input("Enter the course name: ")
        self.course_code = int(input("Enter the course code: "))
        self.instructor_name = input("Enter the instructor name")
        self.course_id = int(input("Enter the course id: "))
        cursor.execute(
            "UPDATE Courses SET course_name = %s, course_code = %s, instructor_name = %s WHERE course_id = %s",
            (self.course_name, self.course_code, self.instructor_name, self.course_id))
        print("Course information has been updated successfully")

        conn.commit()
        conn.close()

    def update_teacher(self):
        conn = self.db_conn_util.makeconnection()
        cursor = conn.cursor()
        self.teacher_id = int(input("Enter teacher id to update"))
        self.first_name = input("Enter first name")
        self.last_name = input("Enter last name")
        self.email = input("Enter email")
        sql = "UPDATE Teacher SET first_name = %s, last_name = %s, email = %s WHERE teacher_id = %s "
        values = (self.first_name, self.last_name, self.email, self.teacher_id)

        print("Teacher information has been updated successfully")

        cursor.execute(sql, values)
        conn.commit()
        conn.close()


obj = DBInteraction()
obj.create_payment()
