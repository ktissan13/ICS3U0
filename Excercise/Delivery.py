# Delivery
# Tissan Kugathas
# ICS 3U0
# March 22 2019

length = int(input("Enter the length of the package: "))
width = int(input("Enter the width of the package: "))
height = int(input("Enter the height of the package: "))

if ((length <= 10 and width <= 10) and height <= 10):
    print("Accept")
else:
    print("Reject")
