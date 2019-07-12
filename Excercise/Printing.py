# Excercise 1 - Printing
# Tissan Kugathas
# ICS 3U0
# March 22 2019

copies = int(input("Enter the number of copies to be printed: "))

if (copies > 0):
    if (copies <= 99):
        cost = float(0.30)
    elif (copies <= 499):
        cost = float(0.28)
    elif (copies <= 749):
        cost = float(0.27)
    elif (copies <= 1000):
        cost = float(0.26)
    elif (copies > 1000):
        cost = float(0.25)
    print("Price per copy is: $", cost)
    Total = cost * copies
    print("Total cost is: $", Total)
        
    

else:
    print("Error")

