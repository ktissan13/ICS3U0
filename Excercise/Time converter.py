# Time Converter
# Tissan Kugathas
# ICS 3U0
# May 22 2019

#--------------------Functions--------------------#

def hours_to_mins():
    hours = float(input("Enter the number of hours: "))
    mins = hours * 60
    print("%.2f %2s %.2f %2s"%(hours, "hours =", mins, "minutes"))

def days_to_hours():
    days = float(input("Enter the number of days: "))
    hours = days * 24
    print("%.2f %2s %.2f %2s"%(days, "days =", hours, "hours"))

def mins_to_hours():
    mins = float(input("Enter the number of minutes: "))
    hours = mins/60
    print("%.2f %2s %.2f %2s"%(mins, "minutes =", hours, "hours"))

def hours_to_days():
    hours = float(input("Enter the number of hours: "))
    days = hours/24
    print("%.2f %2s %.2f %2s"%(hours, "hours =", days, "days"))

#--------------------Instructions--------------------#

print("Enter 1 to convert hours to minutes")
print("Enter 2 to convert days to hours")
print("Enter 3 to convert minutes to hours")
print("Enter 4 to convert hours to days \n")

#--------------------Main Code--------------------#

select = int(input("What do you want to convert: "))

if select == 1:
    hours_to_mins()
elif select == 2:
    days_to_hours()
elif select == 3:
    mins_to_hours()
elif select == 4:
    hours_to_days()
else:
    print("Invalid Choice")
