import math
class circle:

    def __init__(self):
        pass
    def area(self):
        self.radius=int(input("Enter a radius"))
        area=(((self.radius)**2)*(math.pi))
        return area
obj1=circle()

print("The area is "+obj1.area())

        
        