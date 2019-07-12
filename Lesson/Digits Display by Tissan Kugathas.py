# Digits Display
# Tissan Kugathas
# ICS 3U0
# April 8 2019

integer = int(input("Enter a positive integer: "))
place_value = 1
status = True
integer_temp = integer 

while status == True:
    integer_temp = integer_temp - (integer_temp%(10**place_value))
    if integer_temp == 0:
        status = False
    else:
        place_value += 1

while place_value > 0:
    digit = (integer%(10**place_value))//10**(place_value - 1)
    print(digit)
    place_value -= 1

    
    
