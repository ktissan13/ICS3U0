# Investment
# Tissan Kugathas
# ISC 3U0
# April 8th 2019

year = 0
principal = int(input("How much are you putting down: "))
rate = float(input("What is the rate: "))
desire_amount = int(input("How much do you want make your investment worth: "))
amount = 0

while amount < desire_amount:
    year+=1
    amount = principal*((1 + rate)**year)

print(year)
