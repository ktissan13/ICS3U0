# Student Roster
# Tissan Kugathas
# ICS 3U0
# April 30 2019

student_name = []
number_of_students = int(input("Enter the number of students: "))

for current_student in range(number_of_students):
    student_name.append(input("Enter student name: "))

print("Student Roster")

for current_student in range(len(student_name)):
    print(student_name[current_student])
    
