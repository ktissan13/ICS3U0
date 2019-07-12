# Simple Interest
# Tissan Kugathas
# ICS 3U0
# March 6th, 2019

Amount = int(input("Enter the Amount: "))
years = int(input("Enter the number of years: "))
interest_rate = float(input("Enter the interest rate: "))

Principal = Amount / (1 + years * interest_rate)

print("The value after the term is: $"+str("%.2f"%Principal))
