# Loops and string test question 1
# Tissan Kugathas
# ICS 3U0
# April 18 2019

# Prompts user to enter a word
word = str(input("What is the word: ")).upper()
# this variable is used to track the number of letters than can be rotated
can_rotate = 0
# this variable tracks if the word contains a space
number_of_spaces = 0

# this checks if the word is greater than 30
if len(word) > 30:
    # if true then tell user that the word has to be less than 30
    print("Error!, the word has to be less than 30 letters")
# this checks if the word has atleast one character 
elif len(word) == 0:
    # if true then tell user that the word has to contain atleast one character
    print("Error!, the word has to have atleast one character")
else:
    # this loop is used to check each character
    for letter in word:
        # if the character is a space then add one to the number_of_spaces variable
        if letter in ' ':
            number_of_spaces+=1
    # if the number of spaces is greater than 0 then tell user to not have spaces else continue the code
    if number_of_spaces > 0:
        print("Error!, the word can not have spaces")
    else:
        # this loops will check if the word has the letters that can rotate 
        for letter in word:
            # if the letter can be rotated then add 1 to can rotate 
            if letter in 'IOSHZXN':
                can_rotate+=1
        # this checks if the whole word can be rotated
        if len(word) == can_rotate:
            # if all the letter in word can be rotated then tell user that the word can be rotated
            print("Yes, the word can be rotated.")
        else:
            # if not tell the user is cannot be done 
            print("No, the word cannot be rotated.")

