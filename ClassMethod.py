
class Student:
    graduation = "Btech"  # Class variable

    # Class method to display graduation
    @classmethod
    def graduate_in(cls):
        print("Graduation:", cls.graduation)

    # Static method to display roll number
    @staticmethod
    def roll_number(y):
        print("Roll Number:", y)


# Dynamically converting the method to a class method and calling it
Student.graduate = classmethod(Student.graduate_in)
Student.graduate()  
print()

# Calling class method and static method directly via class
Student.graduate_in()  
Student.roll_number(101)  