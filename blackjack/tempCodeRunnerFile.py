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

while input("Enter 'y' to play again or 'n' to exit.") == y:
    print("\n" *20)
    play_game()
