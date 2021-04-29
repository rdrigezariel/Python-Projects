# Parent Class Person
class Person:
    name = "Ariel"
    email = "ariel@gmail.com"
    password = "passw0rd"

    def login(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")

        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

# Child Class Teacher
class Teacher(Person):
    hourly_pay = 15.00
    department = "Science"
    pin_code = "12345"

    def login(self):
        print("\nTeacher Login:")
        entry_name = input("\tEnter your name: ")
        entry_email = input("\tEnter your email: ")
        entry_pin_code = input("\tEnter your pin: ")

        if (entry_email == self.email and entry_pin_code == self.pin_code):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

# Child Class Student
class Student(Person):
    grade = 12
    gpa = 3.5
    pin_code = "54321"

    def login(self):
        print("\nStudent Login:")
        entry_name = input("\tEnter your name: ")
        entry_email = input("\tEnter your email: ")
        entry_pin_code = input("\tEnter your pin: ")

        if (entry_email == self.email and entry_pin_code == self.pin_code):
            print("Welcome back, {}! Your GPA is currently: {}.".format(entry_name, self.gpa))
        else:
            print("The password or email is incorrect.")

teacher = Teacher()
teacher.login()

student = Student()
student.login()
