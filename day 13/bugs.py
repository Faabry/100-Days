# my_function()

# ----------- Reproduce the Bug -------------
'''from random import randint
            # 0    1    2    3    4    5
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"] # Lists starts with "0"
dice_num = randint(1, 6) # or I put:   "dice_num = randint(0, 5)"
print(dice_imgs[dice_num]) # or I put: "print(dice_imgs[dice_num - 1])"


# ------------ Play Computer -----------------
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994: # It's missing an equals signal, because without this
                  # There's no lines to be printed by the program if you type 1994
  print("You are a Gen Z.")

# Fix the Errors
age = input("How old are you?") # The input is considered a str, it's necessary
                                # to convert it like: "int(input("How old are you?"))"
if age > 18:
    print("You can drive at age {age}.") # It's missing the "f" string in the beggning
                                         # It'll print {age} instead of the variable age
#else:
    #print("You can't drive yet.")'''

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)


# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])