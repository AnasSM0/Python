#import random module
import random 
#import art
from art import logo
from art import vs
#import game data
from game_data import data

def compare(data):
    random_num = random.randint(0,49)
    return data["name", "description", "country"][random_num]

#print comparison A
print(logo)
print(f"Comapre A: {data[0]}")
#print VS logo
print(vs)
#print comparsion B
print(f"Comapre B: {data[1]}")
#input choice
choice = input("Who has more followers? Type 'A' or 'B': ")
