# Loops and Strings test Question 2 
# Tissan Kugathas
# ICS 3U0
# April 18 2019

# User inputs the lower limit of range 
lower_limit = int(input("Enter lower limit of range: "))
# User inputs the upper limit of range
upper_limit = int(input("Enter upper limit of range: "))

# Set the number of RSA Number to 0 before the loop starts
RSA_NUMBER = 0;

# This checks if the limits are less than 1000
if (lower_limit > 1000 or upper_limit > 1000):
    # If true then tell user that limit has to be less than 1000
    print("Error!, the limit has to be less than 1000")
# This checks if the lower limit is less then the upper limit
elif (lower_limit > upper_limit):
    #If true then tell user that lower limit is greater than upper limit
    print("Error!, lower limit has to be less than upper limit")
else:
    # This loop will check the numbers from the lower_limit to upper_limit to see if they are RSA numbers
    for current_number in range(lower_limit, upper_limit+1):
        # sets the equal divisor to zero before the loop starts
        equal_divisor = 0;
        # This loop is used to check the what numbers give the current number equal divisor
        for divisor in range(1, current_number +1):
            # If the current number and divisor equals 0 than add one to equal divisor indicating it has a equal divisor
            if current_number%divisor == 0:
                equal_divisor += 1
        # After the loop finished then check if it has 4 equal divisors
        if equal_divisor == 4:
            # if it has 4 then add one RSA number as it is a RSA number 
            RSA_NUMBER += 1
    # Print the number of RSA number found between the lower limit and upper limit 
    print("The number of RSA numbers between", lower_limit, "and", upper_limit, "is", RSA_NUMBER)
