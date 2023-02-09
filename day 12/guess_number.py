from random import randint

game_over = False

def high_or_low(secret_number, guess):
        if guess == secret_number:
            print(f"You got it! \nThe secret number was {secret_number}") 
            global game_over
            game_over = True
        elif guess < secret_number:
            print("Too low")
        elif guess > secret_number:
            print("Too high")
        else:
            print("Enter with a valid number")

choice = {
    "easy": high_or_low,
    "hard": high_or_low
}

secret_number = randint(1, 100)
number_of_tries = 0
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
challenge = input("I'm thinking in a number between 1 and 100" +
                  "Want to play the 'easy' level or 'hard' level? ")

for value in choice:
        if challenge == "easy":
            number_of_tries = 10
        else:
            number_of_tries = 5
# while not game_over or number_of_tries != 0:
while not game_over or number_of_tries == 0:
        print(f"You have {number_of_tries} tries left")
        guess = int(input("Guess a number: "))
        answer = choice[challenge]
        guessed_number = answer(secret_number, guess)
        number_of_tries -= 1



# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
