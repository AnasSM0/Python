from art import logo
import random

def deal():
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(deck)
    return card

def calc_score(deck):
    if sum(deck) == 21 and len(deck) == 2:
        return 0
    
    if 11 in deck and sum(deck) > 21: 
        deck.remove(11)
        deck.append(1)
    return sum(deck)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw."
    elif c_score == 0:
        return"You lose, Opponent got a blackjack."
    elif u_score == 0:
        return "You win with a blackjack!"
    elif c_score > 21:
        return "You win, Opponent went over 21."
    elif u_score > 21:
        return "You lose, You went over 21."
    elif u_score > c_score:
        return "You win!"
    else:
        return "You lose :("

def play_game():
    print(logo)
    user_cards = []
    comp_cards = []
    is_game_over = False
    comp_score = -1
    user_score = -1

    for _ in range(2):
        user_cards.append(deal())
        comp_cards.append(deal())

    while not is_game_over:
        user_score = calc_score(user_cards)
        comp_score = calc_score(comp_cards)
        print(f"Your cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}") 

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True

        else: 
            should_deal = input("\nType 'y' to get another card or 'n' to pass: ")
            print("\n")
            if should_deal == "y":
                user_cards.append(deal())
            else: 
                is_game_over = True


    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal())
        comp_score = calc_score(comp_cards)

    print(f"\nYour final cards: {user_cards}, Final score: {user_score}")
    print(f"\nComputer Final Cards: {comp_cards}, Computer's Final Score: {comp_score}")
    print(compare(user_score,comp_score)) 

while input("\nEnter 'y' to play blackjack or 'n' to exit: ") == "y":
    print("\n" *20)
    play_game()
