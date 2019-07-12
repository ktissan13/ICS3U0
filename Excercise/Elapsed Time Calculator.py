# Elapsed Time Calculator
# Tissan Kuagathas
# ICS 3U0
# April 12 2019

start_hour = int(input("Enter the starting hour: "))
Time_of_day = str(input("Enter am or pm: "))
elapsed_hour = int(input("Enter the number of elapsed hours: "))
current_time = start_hour

while elapsed_hour > 0:
    current_time += 1
    if current_time > 12:
        current_time = 1
    if current_time == 12:
        if Time_of_day == "am":
            Time_of_day = "pm"
        else:
            Time_of_day = "am"
    elapsed_hour -= 1
print("The time is:",str(current_time)+":00",Time_of_day)
