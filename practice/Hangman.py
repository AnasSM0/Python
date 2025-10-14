import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = [
    "python", "developer", "keyboard", "monitor", "laptop", "guitar", 
    "bicycle", "elephant", "umbrella", "chocolate", "backpack", "notebook",
    "rainbow", "penguin", "mountain", "adventure", "mystery", "detective", 
    "sunshine", "moonlight", "telescope", "spaceship", "volcano", "puzzle",
    "whisper", "journey", "dragon", "treasure", "parachute", "ocean", 
    "zebra", "wizard", "football", "painting", "strategy", "castle",
    "waterfall", "jungle", "desert", "carousel", "fireworks", "horizon"
]

lives = 6

random_word = random.choice(word_list)
word_len = len(random_word)

display = ["_"] * word_len
game_over = False

print(" ".join(display))  


while not game_over:
    guess = input("\nGuess a letter: ").lower()

  
    for index, letter in enumerate(random_word):
        if letter == guess:
            display[index] = letter  

    print(" ".join(display)) 

if guess not in random_word:
    lives -= 1
    if lives == 0:
        game_over = True
        print("\nYou Lose! The word was:", random_word)


    if "_" not in display:
        game_over = True
        print("\nYou win! The word was:", random_word)


print("\n",stages[lives])