# Prime Number Part A
# Tissan Kugathas
# ICS 3U0
# April 4 2019

number = int(input("Enter a number: "))
divisor = 2
status = True

if number % 2 == 0:
    status = False
else:
    while divisor < number//2:
        if number % divisor == 0:
            status = False
        divisor += 1

if status == True:
    print(number, "is a prime")
elif status == False:
    print(number, "is not a prime")
    
