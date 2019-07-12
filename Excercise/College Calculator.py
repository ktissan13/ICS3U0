# College Calculator
# Tissan Kugathas
# ICS 3U0
# March 4th, 2019

expenses = float(input("Enter the expenses for your post secondary: "))
offset_cost = float(input("Enter the offset cost for your post secondary: "))

total_cost = expenses - offset_cost

print("The total cost for you post secondary will be: $"+"%.2f"%total_cost)
