# Conditional Control Test Question 3
# Tissan Kugathas
# ICS 3U0
# April 1st 2019

# Ask user the speed limit
speed_limit = int(input("Enter the speed limit: "))
# Ask user the speed that the radar detected
current_speed = int(input("Enter the recorded speed of the car: "))

# if the speed detected is less than the speed limit
# it will tell the user they are going within the speed limit 
if current_speed <= speed_limit:
    print("Congratulations, you are within the speed limit!")
# if the speed dectected is more than the speed limit
elif current_speed > speed_limit:
    # If the user is going going more than 1 over and less than 20 over then
    # They will have to pay $100
    if current_speed <= (speed_limit+20):
        print("You are speeding and your fine is $100")
    # If the user is going going more than 20 over and less than 30 over then
    # They will have to pay $270
    elif current_speed <= (speed_limit+30) and current_speed > (speed_limit+20):
        print("You are speeding and your fine is $270")
    # If the user is going going more than 30 over
    # They will have to pay $500
    elif current_speed > (speed_limit+30):
        print("You are speeding and your fine is $500")
