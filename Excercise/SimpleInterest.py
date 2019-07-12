# Simple Interest
# Tissan Kugathas
# ICS 3U0
# March 6th, 2019

Principal = int(input("Enter the principal: "))
years = int(input("Enter the number of years: "))
interest_rate = float(input("Enter the interest rate: "))

Amount = Principal * (1 + years * interest_rate)

print("The value after the term is: $"+str("%.2f"%Amount))
