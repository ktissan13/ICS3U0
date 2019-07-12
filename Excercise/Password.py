# Password
# Tissan Kugathas
# ICS 3U0
# April 12 2019

password = "msi"
count = 0;

while count < 3:
    user_password = str(input("Enter the password: "))
    if user_password == password:
        print("Welcome")
        break
    else:
        print("The password you typed is incorrect,")
    count += 1
    if count == 3:
        print("Access denied.")

