# Order
# Tissan Kugathas
# ICS 3U0
# March 6th, 2019

burgers = int(input("Enter the number of burgers: "))

fries = int(input("Enter the number of  fries: "))

sodas = int(input("Enter the number of sodas: "))

cost_pretax = burgers*1.69 + fries*1.09 + sodas*0.99
print("Total before tax: $"+str("%.2f"%cost_pretax))

tax = cost_pretax * 0.065

print("Tax: $"+str("%.2f"%tax))

Final_cost = cost_pretax + tax

print("Final Total: $"+str("%.2f"%Final_cost))

cash = float(input("Enter amount tendered: $"))

change = cash - Final_cost

print("Change: $"+str("%.2f"%change))



