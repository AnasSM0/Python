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
    



