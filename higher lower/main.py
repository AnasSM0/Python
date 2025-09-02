import random 
from art import logo
from art import vs
from game_data import data



score = 0
should_continue = True

while should_continue:

    account_a = random.choice(data)
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    def format(account):

        account_name = account["name"]
        description = account["description"]
        country = account["country"]

        return f"{account_name}, A {description} from {country}"

    def check_answer(guess, a_followers,b_followers):
        if a_followers > b_followers:
            return guess == "a"
        else:
            return guess == "b"

    print(logo)

    print(f"Compare A: {format(account_a)}")
    print(vs)
    print(f"Compare B: {format(account_b)}")

    choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(choice,a_follower_count,b_follower_count)

    if is_correct:
        score += 1
        print(f"You're correct. Current score: {score}")
    else: 
        print(f"You're wrong. Final score: {score}")
        should_continue = False
        
