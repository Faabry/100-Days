from random import randint
from art import logo

game_over = False

def high_or_low(secret_number, guess):
        """"Checks if the guessed number is equal to the random number"""
        if guess == secret_number:
            # If they got the answer correct, show the actual answer to the player.
            print(f"You got it! \nThe secret number was {secret_number}") 
            global game_over
            game_over = True # This conditions will allow us to finish the application before finish the amount of tries
        elif guess < secret_number:
            # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
            print("Too low.")
            print("Guess again.")
        elif guess > secret_number:
            print("Too high.")
            print("Guess again.")
        else:
            print("Enter with a valid number .. ")

choice = {
    "easy": high_or_low,
    "hard": high_or_low
}

secret_number = randint(1, 100)
number_of_tries = 0
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
print(logo)
challenge = input("I'm thinking in a number between 1 and 100" +
                  "Want to play the 'easy' level or 'hard' level? ")

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
for value in choice:
        if challenge == "easy":
            number_of_tries = 10
        else:
            number_of_tries = 5
            
# while not game_over or number_of_tries != 0:
while not game_over:
        # Track the number of turns remaining.
        print(f"You have {number_of_tries} tries left")
        guess = int(input("Guess a number: "))
        answer = choice[challenge] # the dict choice in the key of challenge/ it becomes a function
        guessed_number = answer(secret_number, guess)
        number_of_tries -= 1
        # If they run out of turns, provide feedback to the player. 
        if number_of_tries == 0:
             print(f"You've run out of guesses the number was {secret_number}")
             game_over = True


