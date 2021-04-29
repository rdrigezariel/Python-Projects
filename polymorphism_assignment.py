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

# Child Class Teacher (inherits the Person class)
class Teacher(Person):
    hourly_pay = 15.00
    department = "Science"
    pin_code = "12345"

    # This is the same method in the Person class.
    # The difference is that, instead of using entry_password, we're using entry_pin.
    def login(self):
        print("\nTeacher Login:")
        entry_name = input("\tEnter your name: ")
        entry_email = input("\tEnter your email: ")
        entry_pin_code = input("\tEnter your pin: ")

        if (entry_email == self.email and entry_pin_code == self.pin_code):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The password or email is incorrect.")

# Child Class Student (inherits the Person class)
class Student(Person):
    grade = 12
    gpa = 3.5

    # This is the same method in the Person class.
    # The difference is that, instead of using entry_pin as the Teacher class, we use the password inherited in the Person class.
    def login(self):
        print("\nStudent Login:")
        entry_name = input("\tEnter your name: ")
        entry_email = input("\tEnter your email: ")
        entry_password = input("\tEnter your pin: ")

        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}! Your GPA is currently: {}.".format(entry_name, self.gpa))
        else:
            print("The password or email is incorrect.")

#The following code invokes the methods inside each child class for Teacher and Student.

teacher = Teacher()
teacher.login()

student = Student()
student.login()
