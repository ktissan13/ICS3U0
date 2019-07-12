# Conditional Control Test Question 2
# Tissan Kugathas
# ICS 3U0
# April 1st 2019

# Ask user the amount of minutes they talk in the daytime
daytime = int(input("Number of daytime minutes: "))
# Ask user the amount of minutes they talk in the evening 
evening = int(input("Number of evening minutes: "))
# Ask user the amount of minutes they talk in the weekend 
weekend = int(input("Number of weekend minutes: "))

# Plan A
# This part calculates the total cost for Plan A
# First it sets the cost at 0 just in case if the user inputs a number less then free minutes
daytime_A_Cost = 0

# If they talk more then the free minutes
# It will subtract the free minutes and find the total cost 
if daytime > 100:
    daytime_A_Cost = (daytime-100)*0.25

# This finds the total cost in the evening 
evening_A_Cost = evening*0.15

# This finds the total cost in the weekend
weekend_A_Cost = weekend*0.20

# This calculates and rounds the total cost of the plan 
Total_A_Cost = "%.2f"%(daytime_A_Cost + evening_A_Cost + weekend_A_Cost)

# This prints out the total price of the plan to the user 
print("Plan A costs", Total_A_Cost)

# Plan B
# This part calculates the total cost for Plan B
# First it sets the cost at 0 just in case if the user inputs a number less then free minutes
daytime_B_Cost = 0

# If they talk more then the free minutes
# It will subtract the free minutes and find the total cost 
if daytime > 250:
    daytime_B_Cost = (daytime-250)*0.45

# This finds the total cost in the evening    
evening_B_Cost = evening*0.35

# This finds the total cost in the weekend
weekend_B_Cost = weekend*0.25

# This calculates and rounds the total cost of the plan 
Total_B_Cost = "%.2f"%(daytime_B_Cost + evening_B_Cost + weekend_B_Cost)

# This prints out the total price of the plan to the user 
print("Plan B costs", Total_B_Cost)

# Which one is cheeper
# This part is responsible for telling the user which plan is cheaper
# If the Plan A and B are the same price it will tell the user its the same price
if Total_A_Cost == Total_B_Cost:
    print("Plan A and B are the same price.")
# If Plan B is cheaper than Plan A then it will tell the user Plan B is cheaper
elif Total_A_Cost > Total_B_Cost:
    print("Plan B is the cheapest")
# If Plan  A is cheaper than Plan B then it will tell the user Plan A is cheaper 
elif Total_A_Cost < Total_B_Cost:
    print("Plan A is the cheapest")
