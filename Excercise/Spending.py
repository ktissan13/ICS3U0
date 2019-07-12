# Spending
# Tissan Kugathas
# ICS 3U0
# March 6th, 2019

print("Enter the amount spent last month on the following items: \n")

food_cost = int(input("Food: $"))
clothing_cost = int(input("Clothing: $"))
entertainment_cost = int(input("Entertainment: $"))
rent_cost = int(input("Rent: $"))

total_cost = food_cost + clothing_cost + entertainment_cost + rent_cost

food_percent = (food_cost/total_cost)*100
clothing_percent = (clothing_cost/total_cost)*100
entertainment_percent = (entertainment_cost/total_cost)*100
rent_percent = (rent_cost/total_cost)*100

print()
print("%-10s %13s"%("Category", "Budget"))
print("%-10s %13s"%("Food", "%.2f"%food_percent+"%"))
print("%-10s %13s"%("Clothing", "%.2f"%clothing_percent+"%"))
print("%-10s %10s"%("Entertainment", "%.2f"%entertainment_percent+"%"))
print("%-10s %13s"%("Rent", "%.2f"%rent_percent+"%"))


