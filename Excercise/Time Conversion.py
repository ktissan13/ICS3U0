# Time Conversion
# Tissan Kugathas
# ICS 3U0
# March 5th, 2019

time = int(input("Enter the time in minutes: "))

hours = time//60

mins = time - 60*hours

print("The time is:", str(hours)+":"+str(mins))
