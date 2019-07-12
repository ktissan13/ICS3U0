# Palindrome
# Tissan Kugathas
# ICS 3U0
# May 2 2019

string = str(input("Enter a string: "))
forward = []
backward = []

for index in range(len(string)):
    forward.append(string[index])
    backward.append(string[index])


backward.reverse()

palindrome = True

for index in range(len(forward)):
    if str(forward[index]) != str(backward[index]):
        palindrome = False


if palindrome == True:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")
    
