# Counters and Accumulators
# Tissan Kugathas
# ICS 3U0
# Tissan Kugathas

Total = 0
count = 0
value = 1

while(value != 0):
    value = int(input("Enter a value (0 to quit): "))
    Total += value
    if value !=0:
        count += 1

average = Total/count
print("Average is", average)

