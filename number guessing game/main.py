from art import logo
import random     



random_number = random.randint(1,100)
print(logo)
print("\nWelcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Select a difficulty. Type 'easy' or 'hard': ")

attempts = 0

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else: 
    print("Invalid option, Please try again.")

print(f"You have {attempts} attempts left to guess.")
user_guess = int(input("Make a guess: "))

if user_guess < random_number:
    print("Too low. Guess again")
elif user_guess > random_number:
    print("Too high. Guess again")
else:
    print("Invalid choice. Try again.")

if user_guess != random_number:
    attempts - 1
    print(f"You have {attempts} attempts left to guess.")
elif user_guess == random_number:
    print(f"You got it! The answer was {random_number}")
else: 
    print("")
