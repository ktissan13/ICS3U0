#Exercise 1 - Object Height 
#Tissan Kugathas
#ICS 3U0
#March 2nd, 2019

time = float(input("Enter a time less than 4.5 seconds: "))

if time < float(4.5):
    height = 100-4.9*time*2
    print("The height of the object is:", height)
else:
    print("ERROR!")
    print("Next time, enter a value less than 4.5 seconds")

    
