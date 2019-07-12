# Prime Number Part B with for loop
# Tissan Kugathas
# ICS 3U0
# April 5 2019

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
    for current_number in range(number1, number2+1, 1):
        if current_number == 2:
            print(current_number)
        status = True
        divisor = 3
        if current_number % 2 == 0:
            status = False
        else:
            for divisor in range(2, current_number//2, 1):
                if current_number % divisor == 0:
                    status = False
        if status == True:
            print(current_number)
