# Metric Conversions
# Tissan Kugathas
# ICS 3U0
# May 27 2019

def inches_to_centimeters(inches):
    centimeters = inches*2.54
    return centimeters

def feet_to_centimeters(feet):
    centimeters = feet*30
    return centimeters

def yards_to_meters(yards):
    meters = yards*0.91
    return meters

def miles_to_kilometers(miles):
    kilometers = miles*1.6
    return kilometers

def centimeters_to_inches(centimeters):
    inches = centimeters/2.54
    return inches

def centimeters_to_feet(centimeters):
    feet = centimeters/30
    return feet

def meters_to_yards(meters):
    yards = meters/0.91
    return yards

def kilometers_to_miles(kilometers):
    miles = kilometers/1.6



number = int(input("Enter a number: "))

print()
print("Convert: ")
print(("1. Inches to Centimeters","5. Centimeters to Inches"))
