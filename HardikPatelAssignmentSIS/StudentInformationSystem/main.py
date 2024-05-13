from dao.db_interaction import DBInteraction


class MainModule:
    def __init__(self):
        self.db_interaction = DBInteraction()

    def run(self):
        while True:
            print("Student Information Menu")
            print("1. Create Student")
            print("2. Create Course")
            print("3. Create Enrollment")
            print("4. Create Payment")
            print("5. Create Teacher")
            print("6. Update Student")
            print("7. Update Course")
            print("8. Update Enrollment")
            print("9. Update Payment")
            print("10. Update Teacher")
            print("11. Get Student by ID")
            print("12. Get Course by ID")
            print("13. Get Enrollments for Student")
            print("14. Get Enrollments for Course")
            print("15. Get Payments for Student")
            print("16. Get Teacher by ID")
            print("17. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.db_interaction.create_student()

            elif choice == "2":
                self.db_interaction.create_course()

            elif choice == "3":
                self.db_interaction.create_enrollment()

            elif choice == "4":
                self.db_interaction.create_payment()

            elif choice == "5":
                self.db_interaction.create_teacher()

            elif choice == "6":
                self.db_interaction.update_student()

            elif choice == "7":
                self.db_interaction.update_course()

            elif choice == "8":
                self.db_interaction.update_enrollment()

            elif choice == "9":
                self.db_interaction.update_payment()

            elif choice == "10":
                self.db_interaction.update_teacher()

            elif choice == "11":
                self.db_interaction.get_student_by_id()

            elif choice == "12":
                self.db_interaction.get_course_by_id()

            elif choice == "13":
                self.db_interaction.get_enrollments_for_student()

            elif choice == "14":
                self.db_interaction.get_enrollments_for_course()

            elif choice == "15":
                self.db_interaction.get_payments_for_student()

            elif choice == "16":
                self.db_interaction.get_teacher_by_id()

            elif choice == "17":
                print("Thanks for using the Student Information System.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main_module = MainModule()
    main_module.run()
