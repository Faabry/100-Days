from logo import (logo, vs)
from game_data import data
import random
from replit import clear

def format(account):
    """ Format the values inside the data into a printable format """
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, {account_desc}, {account_country}"


def check(guess, a_followers, b_followers):
    """  Checks if the user's guess is right """
    if a_followers > b_followers:
        return guess == "A"             # if answer == "A":
    else:                               #     if amount_followers_a > amount_followers_b:
        return guess == "B"             #         print("Acerto miseravi")
                                        #     else:
                                        #         print("Errou")
                                        # elif answer == "B":
                                        #     if amount_followers_b > amount_followers_a:
                                        #         print("Acerto miseravi")
                                        #     else:
                                        #         print("Errou")
# Display the art logo
print(logo)
game_over = False
current_score = 0
account_b = random.choice(data)

# Keep the game repeatable while the user's not wrong
while not game_over:
    # Generate a random account from the data
    # Make the account B becomes the next account A
    account_a = account_b
    account_b = random.choice(data) # Stores a new random value
    if account_a == account_b:
        account_b = random.choice(data)


    # Ask the user for a guess
    print(f"Compare A: {format(account_a)}")
    print(vs)
    print(f"Compare B: {format(account_b)}")

    answer = str(input("Who has more followers? Type 'A' or 'B':")).upper()[0]

    # Get the amount of followers in the account 
    amount_followers_a = account_a["follower_count"]
    amount_followers_b = account_b["follower_count"]

    is_correct = check(answer, amount_followers_a, amount_followers_b)

    # Clear the screen between the rounds
    clear()
    print(logo)
    
    # Give to the user a feedback with it's guess
    if is_correct:
        # Score kepping
        current_score += 1
        print(f"You're right! Current Score: {current_score}")
        account_a = account_b
        continue
    else:
        print("You're wrong!")
        game_over = True



    


