class Payment:
    def __init__(self, payment_id, student, amount, payment_date):
        self.payment_id = payment_id
        self.student = student
        self.amount = amount
        self.payment_date = payment_date

    def get_payment_id(self):
        return self.payment_id

    def get_student_id(self):
        return self.student.get_student_id()

    def get_amount(self):
        return self.amount

    def get_payment_date(self):
        return self.payment_date
