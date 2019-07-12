# Grade 11 Computer Science Question 2
# Tissan Kugathas
# ICS 3U0
# June 11th 2019

# This is a function which is called if there is input error
def ERROR1():
    print('Invalid Input, Postive Integer')

# list for the depths 
depths = []

# The loop is so that the user can enter 4 depths into the list
for current_depth in range(4):
    depths.append(int(input("Enter depth: ")))

# this is for if the depths increasing then the fish is rising
if depths[0] < depths[1] < depths[2] < depths[3]:
    print('Fish Rising')
# this is for if the depths decreasing then the fish is diving
elif depths[0] > depths[1] > depths[2] > depths[3]:
    print('Fish Diving')
# this is for if the depths are equal then the fish is at a constant depth
elif depths[0] == depths[1] == depths[2] == depths[3]:
    print('Fish At Constant Depth')
# this is if none of the if statments are true then there will be no fish
else:
    print('No Fish')
