import random

word_list = [
    "python", "developer", "keyboard", "monitor", "laptop", "guitar", 
    "bicycle", "elephant", "umbrella", "chocolate", "backpack", "notebook",
    "rainbow", "penguin", "mountain", "adventure", "mystery", "detective", 
    "sunshine", "moonlight", "telescope", "spaceship", "volcano", "puzzle",
    "whisper", "journey", "dragon", "treasure", "parachute", "ocean", 
    "zebra", "wizard", "football", "painting", "strategy", "castle",
    "waterfall", "jungle", "desert", "carousel", "fireworks", "horizon"
]



Random_Word=random.choice(word_list)
print(Random_Word)

word_len=len(Random_Word)
placeholder=""

for letter in range(word_len): 
    placeholder+="_ "
 
print(placeholder)

display=""

while placeholder in display:
    guess = input("\nGuess a letter: ").lower()
    

for i in Random_Word: 
    if i == guess: 
        display += i
    else: 
        display+="_ "


print (display)


