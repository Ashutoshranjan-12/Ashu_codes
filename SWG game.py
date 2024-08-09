"""
Snake, water and gun
snake: 1
water: -1
gun: 0
"""

import random

# Computer randomly chooses a number representing either snake, water, or gun 
computer = random.choice([1,-1,0])
print(" snake: s\n water :w \n gun: g")

# User input for their choice: 's' for snake, 'w' for water, 'g' for gun
youur_choice = input("enter your choice: ")

# Dictionaries to map user input to the corresponding game choice
youDict = {"s":1, "w": -1, "g":0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}

# Get the numerical value for the user's choice
you=youDict[youur_choice]

#  Display both user's and computer's choices
print(f"your choice {reverseDict[you]}\n computer choice {reverseDict[computer]}")

# Determine the outcome of the game
if(computer==you):
    print("its a draw \U0001F600")

else:
    if(computer==1 and you==-1):
        print("you loose\U0001F620")
    
    elif(computer==1 and you == 0):
        print("you win \U0001F602")

    elif(computer==-1 and you ==1):
        print("you win \U0001F602")
    
    elif(computer==-1 and you == 0):
        print("you loose\U0001F620")

    elif(computer==0 and you == 1):
        print("you loose\U0001F620")
    
    elif(computer == 0 and you == -1):
        print("you win \U0001F602")
    else:
        print("something went wrong!")

