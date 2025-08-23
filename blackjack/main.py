from art import logo 
import random

print(logo)

def deal():
    deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(deck)
    return card

def calc_score():
    

user_cards = []
comp_cards = []

for _ in range(2):
    user_cards.append(deal())
    comp_cards.append(deal())


print(user_cards)
print(comp_cards)
