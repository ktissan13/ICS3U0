# Grade 11 Computer Science Question 3
# Tissan Kugathas
# ICS 3U0
# June 11th 2019

# Ask users how many rounds
rounds = int(input("Enter the number of rounds: "))
# Sets the points 100 for each player
Antonia_points = 100
David_points = 100

# Check to see if the rounfs is greater than/equal to 1 and less than/equal to 15
if 1 <= rounds <= 15:
    # Loop so it runs for the rounds the user inputed
    for current_round in range(rounds):
        # Ask the user to enter the roll of Antonia for that round, followed by a space, followed by the roll of David for that round.
        user_input = str(input("Enter the roll of Anotonia, followed by a space enter the roll of David: "))
        # Splits the points into two different elements of a list
        points = user_input.split(' ')
        # Checks to see if antonia roll is less than davids 
        if int(points[0]) < int(points[1]):
            # if true then it substracts david's roll from antonia's current points
            Antonia_points -= int(points[1])
        # Checks to see if david roll is less than antonia
        elif int(points[0]) > int(points[1]):
            # if true then it substracts antonia's roll from david's current points
            David_points -= int(points[0])
    # Prints the total points of each player
    print('Antonia:', Antonia_points)
    print('David:', David_points)
