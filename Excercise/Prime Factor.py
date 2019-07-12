# Prime Factor
# Tissan Kugathas
# ICS 3U0
# April 4 2019

number = int(input("Enter a number: "))
counter = 2

if number <= 0:
    print("Enter a number greater than 0")
else:
    while counter <= number:
        if number % counter == 0:
            print(counter)
            number = number / counter
            counter = 2
        else:
            counter += 1
            
        
        
