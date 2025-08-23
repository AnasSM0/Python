import art
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


user_cards = []
comp_cards = []
is_game_over = False

for _ in range(2):
    user_cards.append(deal())
    comp_cards.append(deal())

user_score = calc_score(user_cards)
comp_score = calc_score(comp_cards)
print(f"Your cards: {user_cards}, Current Score: {user_score}")
print(f"Computer's first card: {comp_cards[0]}") 

#if user_score == 0 or comp_score == 0 or user_score > 21:
#  is_game_over = True



