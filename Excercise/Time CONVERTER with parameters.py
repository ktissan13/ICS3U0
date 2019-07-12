# Time Converter
# Tissan Kugathas
# ICS 3U0
# May 22 2019

#--------------------Functions--------------------#

def hours_to_mins(hours):
    mins = hours * 60
    return mins

def days_to_hours(days):
    hours = days * 24
    return hours 

def mins_to_hours(mins):
    hours = mins/60
    return hours

def hours_to_days(hours):
    days = hours/24
    return days 

#--------------------Instructions--------------------#

print("Enter 1 to convert hours to minutes")
print("Enter 2 to convert days to hours")
print("Enter 3 to convert minutes to hours")
print("Enter 4 to convert hours to days \n")

#--------------------Main Code--------------------#

select = int(input("What do you want to convert: "))

if select == 1:
    hours = float(input("Enter the number of hours: "))
    mins = hours_to_mins(hours)
    print("%.2f %2s %.2f %2s"%(hours, "hours =", mins, "minutes"))
    
elif select == 2:
    days = float(input("Enter the number of days: "))
    hours = days_to_hours(days)
    print("%.2f %2s %.2f %2s"%(days, "days =", hours, "hours"))
    
elif select == 3:
    mins = float(input("Enter the number of minutes: "))
    hours = mins_to_hours()
    print("%.2f %2s %.2f %2s"%(mins, "minutes =", hours, "hours"))
    
elif select == 4:
    hours = float(input("Enter the number of hours: "))
    hours_to_days()
    print("%.2f %2s %.2f %2s"%(hours, "hours =", days, "days"))
else:
    print("Invalid Choice")
