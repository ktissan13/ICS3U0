# Digits - Excercise 7
# Tissan Kugathas
# ICS 3U0
# March 5th, 2019

number = int(input("Enter a three-digit number: "))

hundreds = number//100

remainder = number%100

tens = remainder//10

units = remainder%10

print("The hundreds-place digit is:", hundreds)
print("The tens-place digit is:", tens)
print("The ones-place digit is:", units)
