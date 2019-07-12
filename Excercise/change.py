# Change
# Tissan Kugathas
# ICS 3U0
# March 5th, 2019

cents = int(input("Enter the change in cents: "))

quarters = cents//25

remainder1 = cents - 25*quarters

dimes = remainder1//10

remainder2 = remainder1 - 10*dimes

nickles = remainder2//5

pennies = remainder2 - 5*nickles

print("The minimum number of coins is:")
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickles)
print("Pennies:", pennies)
