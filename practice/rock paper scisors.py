Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
 
Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


Scissors= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random

print("Welcome to Rock, Paper, Scisors.")
choice = int(input ("Select 0 for Rock, 1 for Paper and 2 for Scisors: "))

randomChoice = random.randint(0,2)

if choice !=0 or choice !=1 or choice !=2: 
    print("Invalid Choice. Please Try Again.")

if choice == 0 and randomChoice == 2: 
    print("You Chose: \n" + Rock + "\n Computer Chose: \n" + Scissors) 
    print("You win!")

elif choice == 0 and randomChoice == 1: 
    print("You Chose: \n" + Rock + "\n Computer Chose: \n" + Paper) 
    print("You lose!")

elif choice == 0 and randomChoice == 0: 
    print("You Chose: \n" + Rock + "\n Computer Chose: \n" + Rock)
    print("Game Tie!")


if choice == 1 and randomChoice == 0: 
    print("You Chose: \n" + Paper + "\n Computer Chose: \n" + Rock) 
    print("You win!")

elif choice == 1 and randomChoice == 2: 
    print("You Chose: \n" + Paper + "\n Computer Chose: \n" + Scissors) 
    print("You lose!")

elif choice == 1 and randomChoice == 1: 
    print("You Chose: \n" + Paper + "\n Computer Chose: \n" + Paper)
    print("Game Tie!")


if choice == 2 and randomChoice == 1: 
    print("You Chose: \n" + Scissors + "\n Computer Chose: \n" + Paper) 
    print("You win!")

elif choice == 2 and randomChoice == 0: 
    print("You Chose: \n" + Scissors + "\n Computer Chose: \n" + Rock) 
    print("You lose!")

elif choice == 2 and randomChoice == 2: 
    print("You Chose: \n" + Scissors + "\n Computer Chose: \n" + Scissors)
    print("Game Tie!")



