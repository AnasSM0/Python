print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("\nWelcome to treasure Island.")
print("Your mission is to find the treasure.")

crossRoad = input("\n\nYou are at a cross road where do you want to go? \nLeft or Right? ")

if crossRoad == 'Left' or crossRoad=='L': 
    Lake = input('''\nYou have come to lake. There is an island in the middle of the lake 
\nType "wait" to wait for a boat. Type "swim" to swim across.
\nChoose your option: ''')

else: 
    print("You fell into a hole. Game Over!")

if Lake == 'wait':
    door = input('''\nYou have come across three doors. Red, Yellow and Blue
    \nChoose One: ''')

if door == 'red' or door == 'Red':
    print("You were burned by fire. Game Over!")

elif door ==  'blue' or door == 'Blue':
    print("You got eaten by beasts. Game Over!") 

elif door == 'yellow' or door == 'Yellow':
    print("You chose the right door. You Win!")

else: 
    print("Invalid Option. Game Over!")