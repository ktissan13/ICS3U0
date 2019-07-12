# Even and Odds
# Tissan Kugathas
# ICS 3U0
# May 1 2019

import random
even = []
odd = []

for current_number in range(25):
    number = random.randint(0,99)
    if number%2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("ODD:")
print(odd)
print("EVEN:")
print(even)
