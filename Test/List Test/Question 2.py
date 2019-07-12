# List Test Question 2
# Tissan Kugathas
# ICS 3U0
# May 21 2019

# Prompts the user to enter the K value
# K represents as a parameter as stated in the question
K = int(input("Enter the K value: "))

# If k is less than 10 then continue the code
if K < 10:
    # Prompts the user to enter the string
    string = input("Enter the string that needs to be decoded: ")
    
    # This makes sure the string is uppercased just in case the user inputs lowercase 
    string = string.upper()

    # This checks if the string is less than 20 characters then it will continue the code 
    if len(string) <= 20:
        # This list is create to store the decoded letters
        decoded = []
        # P represents the position of the letter as stated in the question
        P = 1
        # this loop 
        for letter in string:
            # this finds the S value
            # the S value represents the shift value as stated in the question
            S = 3*P+K
            # sets the letter to new letter in order for loop to work
            new_letter = letter
            # loop runs for S value times
            for character in range(S):
                # finds the next letter 
                new_letter = chr(ord(new_letter)-1)
                # if the shift goes further than A then switch it to Z
                if new_letter == '@':
                    new_letter = 'Z'
            # Adds the new_letter to the list
            decoded.append(new_letter)
            # increases the P value by 1
            P += 1
        # Empty variable so that we can put the decoded string together
        decoded_string = ''
        # get each letter then adds it into the empty variable to put into one string
        for letter in decoded:
            decoded_string = decoded_string + letter
        # prints decoded string to the user
        print(decoded_string)
    # This tells the user if the string has to be less than 20 characters if the user inputs more than 20
    else:
        print("ERROR!, String has to be less than 20 characters")

# K is not less than 10 then tell user that it has to be less than 10
else:
    print("ERROR!, K has to be less than 10")


