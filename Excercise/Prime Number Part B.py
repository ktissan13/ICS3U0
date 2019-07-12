# Prime Number Part B
# Tissan Kugathas
# ICS 3U0
# April 4 2019

number1 = int(input("Enter a number to start with: "))
number2 = int(input("Enter a number to end with: "))
divisor = 3
status = True
current_number = number1

if number1 < 2:
    print("Start with a number greater than 2")
elif number1 >= number2:
    print("Enter a end number greater than than the start number")
else:
    while current_number <= number2:
        status = True
        divisor = 3
        if current_number % 2 == 0:
            status = False
        else:
            while divisor < (current_number//2):
                if current_number % divisor == 0:
                    status = False
                divisor += 1
        if status == True:
            print(current_number)
        current_number += 1
    
