"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""


import math

num1 = float(input("Please input your first number: "))

num2 = float(input("Please input your first number: "))

option = input("Is one of the numbers a hypotenuse of a right triangle? (Y/N):  ")

if option == "Y":
    print("didnt have time to finish")
else:
    st1 = math.pow(num1,2) + math.pow(num2,2)
    answer = math.sqrt(st1)
    round(answer,1)
    print(answer)
    







