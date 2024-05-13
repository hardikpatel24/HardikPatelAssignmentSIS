from entity.model import Enrollment
from util.db_conn_util import DBConnectivity

class ServiceProvider:
    def __init__(self):
        self.db_conn_util = DBConnectivity()

    def enroll_in_course(self, enrollment_id, student_id, course_id, enrollment_date):
        try:
            conn = self.db_conn_util.makeconnection()
            cursor = conn.cursor()
            sql = "INSERT INTO Enrollments (enrollment_id, student_id, course_id, enrollment_date) VALUES (%s, %s, %s, %s)"
            values = (enrollment_id, student_id, course_id, enrollment_date)
            cursor.execute(sql, values)
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(str(e))
            return False

s = ServiceProvider()
s.enroll_in_course(1, 1, 1, '2022-09-01')
