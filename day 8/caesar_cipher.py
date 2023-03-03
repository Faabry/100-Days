alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z", "a", "b", "c", "d",
            "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
            "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def caesar(start_text, shift_amount, direction):
    end_text = ""
    if direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char #With no modification for spaces or symbols
    print(f"The {direction} text is {end_text}")


continue_now = True

while continue_now:
    option = str(input("Type 'encode' to encrypt\ 'decode' to decrypt:\n>>>"))
    original_word = str(input("Type the word to be encoded\decoded:\n>>>"))
    shift_amount = int(input("Enter with the number of the shift\n>>>"))

    shift_amount = shift_amount % 26

    caesar(original_word, shift_amount, option)

    question = str(input("Want to go again?\n'yes'/'no'\n>>>"))
    if question == "yes":
        continue
    else:
        print("Good bye")
        break
