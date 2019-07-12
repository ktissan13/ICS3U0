# Functions and Parameters
# Tissan Kugathas
# ICS 3U0
# May 23 2019

import math

#---------------------------Functions---------------------------#

def Area_of_Circle(radius):
    area_of_circle = math.pi*(radius**2)
    return area_of_circle

def Area_of_Rectangle(length, width):
    area_of_rectangle = length * width
    return area_of_rectangle 

#---------------------------Instructions---------------------------#

print("Enter 1 to find the area of a Circle")
print("Enter 2 to find the area of a Rectangle \n")

#---------------------------Main Code---------------------------#

choice = int(input("Which shape do you find the area for: "))

if choice == 1:
    radius = float(input("Enter the radius of the circle: "))
    Area = Area_of_Circle(radius)
    print("The area of the Circle is", "%.2f"%(Area))
if choice == 2:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    Area = Area_of_Rectangle(length, width)
    print("The area of the Rectangle is" , "%.2f"%(Area))
