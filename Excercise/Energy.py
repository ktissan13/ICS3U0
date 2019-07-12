# Energy
# Tissan Kugathas
# ICS 3U0
# March 4th, 2019

mass = float(input("Enter the mass in kilograms: "))

speed_of_light = float(3.0*(10**8))

energy = mass*(speed_of_light**2)

print("The energy produced in Joules is =", "%.1E"%energy)

number_of_light_bulbs = energy/360000

print("The number of 100-watt light bulbs powered =", "%.1E"%number_of_light_bulbs)
