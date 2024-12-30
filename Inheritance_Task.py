class Area:
    pi = 3.14  # Class variable shared among all instances
    def __init__(self, radius):
        self.radius = radius  # Initialize radius - instance variable
        
    def accept_method(self):
        pass  
        
class Circle(Area):
    def __init__(self):  
        radius = float(input("Enter the radius of the circle: "))  # Take input from the user
        super().__init__(radius)  # Initialize the parent class with the user-provided radius
    
    def area_of_circle(self):
        print(f'Radius of circle is {self.radius} and is {self.radius * self.radius * self.pi}')
        

print(Area.pi)


new_circle = Circle()
new_circle.area_of_circle()
