import random
from replit import clear
import art


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
def deal_cards():
    """"Returns a random card from the desk."""
            #A                                J   Q   K
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user, computer):
    if user == computer:
        print("It's a draw")
    elif computer == 0:
        print("Computer has a blackjack!")
    elif user == 0:
        print("You has a blackjack")
    elif user > 21 or user > computer:
        print("Computer wins")
    elif computer > 21 or computer > user:
        print("You win")
    elif user > computer:
        print("You win")
    else:
        print("Computer win")
    print(f"User Score: {user}")
    print(f"Computer Score: {computer}")


def play_game():
    print(art.logo)
    #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().

    user_cards = []
    computer_cards = []

    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

    for _ in range(2):
            user_cards.append(deal_cards())
            computer_cards.append(deal_cards())

    game_over = False

    while not game_over:   
        total_user = calculate_score(user_cards)
        total_computer = calculate_score(computer_cards)
        print(f"User cards: {user_cards}, Current Score: {total_user}")
        print(f"First computer cards: {computer_cards[0]}")

        if total_user >= 21 or total_user == 0 or total_computer >= 21:
            print("The game has ended")
            game_over = True

        #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

        #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
        else:
            answer = str(input("Type 'y' for another card, or 'n' to pass\n>>>")).lower()[0]
            if answer == "y":
                user_cards.append(deal_cards())
            else:
                game_over = True

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while total_computer != 0 and total_computer < 17:
        computer_cards.append(deal_cards())
        total_computer = calculate_score(computer_cards)

    compare(total_user, total_computer)

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


while input("Do you wanna play blackjack? 'y', 'n'") == 'y':
    clear()
    play_game()