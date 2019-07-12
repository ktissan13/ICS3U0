# Grade 11 Computer Science Question 1
# Tissan Kugathas
# ICS 3U0
# June 11th 2019

# This function is for the error function
def ERROR1():
    print("ERROR, Invalid input")

# this gets the total_number of steps taken by Nikky
def Nikky(a,b,s):
    # This sets the current_steps to equal S
    current_steps = s
    # This is the number of steps that is take after
    steps_after = a-b+a-b
    # this add the total number of steps taken
    total_steps = current_steps + steps_after
    # this returns the total number of steps made by the person
    return total_steps

# this gets the total_number of steps taken by Byron   
def Byron(a,b,s):
    # This sets the current_steps to equal S
    current_steps = s
    # This is the number of steps that is take after
    steps_after = a-b+a-b
    # this add the total number of steps taken
    total_steps = current_steps + steps_after
    # this returns the total number of steps made by the person
    return total_steps

# this ask the user to input the value
a = int(input("Give value for a: "))
# this checks if the value is acceptable
if 1 <= a <= 100:
    # this ask the user to input the value
    b = int(input("Give value for b: "))
    # this checks if the value is acceptable
    if 1 <= b <= 100 and a >= b:
        # this ask the user to input the value
        c = int(input("Give value for c: "))
        # this checks if the value is acceptable
        if 1 <= c <= 100:
            # this ask the user to input the value
            d = int(input("Give value for d: "))
            # this checks if the value is acceptable
            if 1 <= d  <= 100 and c >= d:
                # this ask the user to input the value
                s = int(input("Give value for s: "))
                # this checks if the value is acceptable
                if 1 <= s <= 1000:
                   # This calls the nikky function to get the total amout steps
                   Nikky_steps = Nikky(a,b,s)
                   # This calls the byron function to get the total amout steps
                   Byron_steps = Byron(c,d,s)
                   # This check if nikky has more steps then byron then it will print nikky if true
                   if Nikky_steps > Byron_steps:
                       print('Nikky')
                   # This check if Byron has more steps then nikky then it will print byron if true
                   elif Byron_steps > Nikky_steps:
                       print('Byron')
                   # This will check if the have equal amount of steps which means they tied
                   elif Byron_steps == Nikky_steps:
                       print('Tied')
            # this run the ERROR1 function to inform the user the values are invalid
            else:
                ERROR1()
        # this run the ERROR1 function to inform the user the values are invalid
        else:
            ERROR1()
    # this run the ERROR1 function to inform the user the values are invalid
    else:
        ERROR1()
# this run the ERROR1 function to inform the user the values are invalid
else:
    ERROR1()
