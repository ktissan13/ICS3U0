# Discriminat
# Tissan Kugathas
# ICS 3U0
# March 21 2019

A = int(input("Enter the value for A: "))
B = int(input("Enter the value for B: "))
C = int(input("Enter the value for C: "))

Discriminat = (B**2) - (4*A*C)

if Discriminat < 0:
    print("No roots")
elif Discriminat == 0:
    print("One root")
elif Discriminat > 0:
    print("Two roots")
