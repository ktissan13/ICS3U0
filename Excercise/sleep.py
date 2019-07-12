# Sleep
# Tissan Kugathas
# ICS 3U0
# March 5th, 2019

print("Enter your birthdate:")
birth_year = int(input("Year: "))
birth_month = int(input("Month: "))
birth_day = int(input("Day: "))

print("Enter today's date:")
todays_year = int(input("Year: "))
todays_month = int(input("Month: "))
todays_day = int(input("Day: "))

diff_year = (todays_year - birth_year)*365

diff_month = (birth_month - todays_month)*30

diff_day = birth_day - todays_day

total_days = diff_year - diff_month - diff_day

print("You have been alive for", total_days, "days.")

total_hours_slept = total_days * 8

print("You have slept", total_hours_slept, "hours.")
