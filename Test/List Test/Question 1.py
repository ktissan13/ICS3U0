# Lists Test Question 1
# Tissan Kugathas
# ICS 3U0
# May 21 2019

# Prompts the user to enter the first 2 numbers 
sequence = input("Give the first 2 numbers of the sequence separated by a space: ")

# Splits the numbers by a space
numbers = sequence.split(" ")

# checks if the input is valid 
if 0 < int(numbers[1]) < int(numbers[0]) < 10000:
    # Sets the status for while loop to true to run the loop
    status = True
    # Sets the index to 0 as 0 is the first element in a list
    index = 0
    # loop to generate the sumac sequence 
    while (status):
        # makes the next element of the list the difference of the preceding two terms
        numbers.append(int(numbers[index]) - int(numbers[index+1]))
        # terminates when the current number is greater than last number generated 
        if int(numbers[index+1]) < int(numbers[index+2]):
            # sets the loop status to False to stop the loop
            status = False
        else:
            # if doesn't need to terminate, it will increase the index by 1 to find the next element
            index += 1
    # After generating the numbers, it will print it to the user
    print("The resulting sumac sequence is", numbers)
else:
    # if the numbers are not vaild then tell user to input valid inputs
    print("Invalid Input")
