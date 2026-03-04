radius=int(input("Enter a radius for your circle."))

options=int(input("Enter 1 if you want the circumference of the circle, and enter 2 if you want the area of the circle."))

def circumference():
    return (2*radius*3.14)
def area():
    return (radius*radius*3.14)

if options==1:
    print("The circumference is",circumference())
elif options==2:
    print("The area is",area())
else:
    options=int(input(("Try again")))
