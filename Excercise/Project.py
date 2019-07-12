# Project
# Tissan Kugathas
# ICS 3U0
# March 6th, 2019

print("Enter the number of minutes spent on each of the following project task: \n")

designing_min = int(input("Designing: "))
coding_min = int(input("Coding: "))
debugging_min = int(input("Debugging: "))
testing_min = int(input("Testing: "))

total_time = designing_min + coding_min + debugging_min + testing_min

designing_percent = (designing_min/total_time)*100
coding_percent = (coding_min/total_time)*100
debugging_percent = (debugging_min/total_time)*100
testing_percent = (testing_min/total_time)*100

print()
print("%-10s %8s"%("Task", "% Time"))
print("%-10s %8s"%("Designing", "%.2f"%designing_percent+"%"))
print("%-10s %8s"%("Coding", "%.2f"%coding_percent+"%"))
print("%-10s %8s"%("Debugging", "%.2f"%debugging_percent+"%"))
print("%-10s %8s"%("Testing", "%.2f"%testing_percent+"%"))

