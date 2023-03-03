import random

# ----- Mainly Program ------
print("Welcome to the password generator")

# ---- Creating lists to receive letters, numbers and symbols -----
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['@', '!', '$', '*', '-', '+']

# ---- Creating an input to the user inform the amount of each char ----
number_of_letters = int(input("How many letter do you want to yout password? \n"))
number_of_numbers = int(input("How many numbers? \n"))
number_of_symbols = int(input("How many symbols? \n"))

# ---- Creating a list to receive the amount of each variable ----
password = []

# ---- As an integer, it's not necessary to use the 'len' function ----
for c in range(0, number_of_letters): 
    password.append(random.choice(letters))

for c in range(0, number_of_numbers):
    password += random.choice(numbers)

for c in range(0, number_of_symbols):
    password += random.choice(symbols)

# ------------ Printing the password in order -----------
# print(password)

# ------- Creating a shuffle in the item's order --------
random.shuffle(password)

hard_password = ''
for item in password:
    hard_password += item

print(f"Your password is >> {hard_password} <<")











