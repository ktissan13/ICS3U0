# Prime Number Part A with For Loop
# Tissan Kugathas
# ICS 3U0
# April 5 2019

number = int(input("Enter a number: "))
divisor = 2
status = True

if number % 2 == 0:
    status = False
else:
    for divisor in range(2, number//2, 1):
        if number % divisor == 0:
            status = False

if status == True:
    print(number, "is a prime")
elif status == False:
    print(number, "is not a prime")
    
