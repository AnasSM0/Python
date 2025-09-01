from art import logo
import random     

Easy_Attempts = 10
Hard_Attempts = 5

def select_difficulty():

    difficulty = input("Select a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        return Easy_Attempts
    else :
        return Hard_Attempts


def check_answer(user_gue, random_num,turns):
    if user_gue < random_num:
        print("Too low. Guess again")
        return turns - 1
    elif user_gue > random_num:
        print("Too high. Guess again")
        return turns - 1
    else:
        print(f"You got it! The answer was {random_num}")

def game():
    random_number = random.randint(1,100)
    print(logo)
    print("\nWelcome to the number guessing game")
    print("I'm thinking of a number between 1 and 100")

    turns = select_difficulty()

    user_guess = 0

    while user_guess != random_number:
        
        print(f"You have {turns} attempts left to guess.")
        user_guess = int(input("Make a guess: "))
        turns = check_answer(user_guess,random_number,turns)
        

        if turns == 0:
            print("You have run out of guesses, you lose :(")
            return 


game()