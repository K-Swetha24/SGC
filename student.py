class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display_student(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)