# Math Tutor
# Tissan Kugathas
# ICS 3U0
# March 26 2019

import random

randomNum1 = random.randint(1,10)
randomNum2 = random.randint(1,10)
randomOperator = random.randint(1,4)

if (randomOperator == 1):
    print("What is", str(randomNum1), "*", str(randomNum2)+"?")
    user = float(input())
    answer = float(randomNum1 * randomNum2)
elif (randomOperator == 2):
    print("What is", str(randomNum1), "+", str(randomNum2)+"?")
    user = float(input())
    answer = float(randomNum1 + randomNum2)
elif (randomOperator == 3):
    print("What is", str(randomNum1), "-", str(randomNum2)+"?")
    user = float(input())
    answer = float(randomNum1 - randomNum2)
elif (randomOperator == 4):
    print("What is", str(randomNum1), "/", str(randomNum2)+"?")
    user = float(input())
    answer = float(randomNum1 / randomNum2)

if user == answer:
    print("Correct")
else:
    print("Incorrect, answer is", answer)
