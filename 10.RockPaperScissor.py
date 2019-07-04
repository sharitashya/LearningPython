'''
Author - Shreeyash Haritashya
Date - 4th July 2019
Description - Programming rock paper and scissors game in Python
'''
import random

# 0 = rock 
# 1 = paper 
# 2 = scissor 

computer = random.randint(0, 2)
player   = input("Enter your choice: \n rock \n paper \n scissor \n")

if (computer == 0):
    c_move = "rock"
elif (computer == 1):
    c_move = "paper"
else:
    c_move = "scissor"

print("Computer plays - " + c_move)

if (player == "rock"):
    if (computer == 1):
        print("Computer wins!!")
    elif(computer == 2):
        print("You won!!")
    else:
        print("It's a tie.")
elif (player == "paper"):
    if (computer == 2):
        print("Computer wins!!")
    elif(computer == 0):
        print("You won!!")
    else:
        print("It's a tie.")
elif (player == "scissor"):
    if (computer == 0):
        print("Computer wins!!")
    elif(computer == 1):
        print("You won!!")
    else:
        print("It's a tie.")
       
