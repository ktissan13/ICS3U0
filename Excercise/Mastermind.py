# Mastermind
# Tissan Kugathas
# ICS 3U0
# May 8 2019

import random

number_of_pegs = int(input("Enter the number of pegs <1-10>: "))
number_of_colors = int(input("Enter the number of colors <1-10>: "))
print()
pegs = []

if 0<number_of_pegs<11 and 0<number_of_colors<11:
    last_num = 0
    for index in range(number_of_pegs):
        status = True 
        while(status):
            randnum = random.randint(1,number_of_colors)
            if last_num != randnum:
                status = False
        last_num = randnum
        pegs.append(randnum)
    unbroken = True
    Guess = 1
    while(unbroken):
        print("Guess", str(Guess)+":")
        pegs_found = 0
        colors_found = 0
        user_guess = []
        for index in range(len(pegs)):
            current_peg = index+1
            user_input = int(input("Color for peg {}: ".format(current_peg)))
            if user_input == 2002:
                print(pegs)
            user_guess.append(user_input)
        for index in range(len(pegs)):
            if pegs[index] == user_guess[index]:
                pegs_found += 1
        for color in pegs:
            for color_guess in user_guess:
                if color == color_guess:
                    colors_found += 1
        print("You have", pegs_found,"peg(s) correct and", colors_found,"color(s) correct. \n")
        if pegs_found == len(pegs):
            print("You have broken the code in", Guess,"guesses.")
            unbroken = False
        else:
            Guess=int(Guess)+ 1
else:
    print("Invalid input")
