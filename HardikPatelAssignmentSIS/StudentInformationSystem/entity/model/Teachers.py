class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email, expertise):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.expertise = expertise
        self.assigned_courses = ()

    def get_teacher_id(self):
        return self.teacher_id

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_expertise(self):
        return self.expertise

    def get_assigned_courses(self):
        return self.assigned_courses

    def update_teacher_info(self, first_name, last_name, email, expertise):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.expertise = expertise

    def display_teacher_info(self):
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Expertise: {self.expertise}")

    def get_assigned_courses(self):
        return self.assigned_courses
