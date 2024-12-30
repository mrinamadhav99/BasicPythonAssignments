# BASE CLASS OR PARENT CLASS.

class Person:
    def __init__(self, idCard, name):
        self.idCard = idCard
        self.name = name
        
    def displayinfo(self):  # Add `self` as the first parameter
        print(f'Name: {self.name}, Id Card: {self.idCard}')  # Use `self.name` and `self.idCard`


# child class creation for inheritance - Employee class 

class Employee(Person):
    # def __init__(self, idCard, name):
    #     super().__init__(idCard, name)
    pass
    def show(self):
        print("show")



# Example usage
person = Person(1234,'Kasturi chawre')
person.displayinfo() 

obj1 = Employee(122312,"mrinal madhav")
obj1.displayinfo()
obj1.show()
