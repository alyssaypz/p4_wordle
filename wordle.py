import random

possible_words = ["reach", "train", "skate", "lover", "quart", "steel"]



word =  random.choice(possible_words)

# colors for printing
default = '\033[0m'
green = '\033[92m'
yellow = '\033[33m'

# print(green + "hello")

def generate_hint(guess):
    hint = ""
    color = default
    for i in range(5):
        if (guess[i] == word[i]):
            color = green 
        elif guess[i] in word:
            color = yellow
        else:
            color = default 
        hint = hint + color + guess[i] + default
    return hint

def game_loop():
    user_guess = ""
    for i in range(6):
        user_guess = input("Give a guess: ")
        print(generate_hint(user_guess))
        if user_guess == word:
            print("Congratulations")
            break 

game_loop()
