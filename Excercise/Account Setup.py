# Account Setup
# Tissan Kugathas
# ICS 3U0
# April 10th 2019

username = input("Enter a user name: ")
password = input("Enter a password that is at least 8 characters: ")

while len(password) < 8:
    password = input("Enter a password that is at least 8 characters: ")

print("Your user name is", username.lower(),"and your password is", password.lower()+".")
