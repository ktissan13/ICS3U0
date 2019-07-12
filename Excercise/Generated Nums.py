# Generated Nums
# Tissan Kugathas
# ICS 3U0
# May 1 2019

in_range = 102
generated_numbers = []

for current_index in range(in_range):
    number= current_index + current_index//10 + current_index - ((current_index//10)*10)
    generated_numbers.append(number)

print("%-10s %13s"%("Index", "Generated Numbers"))

for index in range(in_range):
    print("%-10s %-13s"%(index, generated_numbers[index]))
