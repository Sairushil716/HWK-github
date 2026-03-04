from math import cos
from math import sin
from math import tan
userangle=int(input("Enter angle"))
userside=input("What side is given?")
usersidelength=int(input("What is the length of that side?"))
outputside="What side do we need to work out?"

if userside.lower()=="adjacent":
    if outputside.lower()=="hypotenuse":
        outputside=usersidelength/cos(userangle)
    if outputside.lower()=="opposite":
        outputside=usersidelength/cos(userangle)
