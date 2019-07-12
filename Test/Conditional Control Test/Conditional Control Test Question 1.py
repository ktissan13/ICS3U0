# Conditional Control Test Question 1
# Tissan Kugathas
# ICS 3U0
# April 1st 2019

# Ask user to enter the numerical month
month = int(input("Give the month: "))
# Ask user to enter the numerical day
day = int(input("Give the day: "))

# First it checks if user input is valid
# If it is not valid then it warn the user that its invalid
# If the user month is between 1 to 12 and day is between 1 and 31 then continue
# if not print Error
if month <= 12 and month >= 1 and day >= 1 and day <= 31:
    # If the month is before February print Before the special day
    if month < 2:
        print("Before")
    # If the month is after February print After the special day
    elif month > 2:
        print("After")
    # If the month is on February continue
    elif month == 2:
        # if the day is before the 18th then print before the special day
        if day < 18:
            print("Before")
        # if the day is after the 18th then print after the special day
        elif day > 18:
            print("After")
        # if the day is on the 18th then print it is the special day
        elif day == 18:
            print("Special")
else:
    # prints if the user inputs an invalid integer 
    print("Error Invalid input")
       
            
