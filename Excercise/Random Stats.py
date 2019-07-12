# Random Stats
# Tissan Kugathas
# ICS 3U0
# May 1 2019

import random
in_range = 501
numbers= []

for index in range(in_range):
    numbers.append(random.randint(0,9))
    
print("%-10s %10s"%("Index", "Occurrences"))

for current_number in range(10):
    occurrences = 0
    for index in range(in_range):
        if numbers[index] == current_number:
            occurrences += 1
    print("%-10s %-10s"%(current_number, occurrences))
    
