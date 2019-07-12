#Excercise 2 - Pizza Cost
#Tissan Kugathas
#ICS 3U0
#March 2nd, 2019

diameter = float(input("Enter the diameter of the pizza in inches: "))

if diameter > 0:
    cost = 0.05*(diameter**2)+1.75
    print("The cost of making the pizza is: $",cost)
else:
    print("The diameter of the pizza has to be greater than 0.")
