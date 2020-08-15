import string
import sys
import requests

chosen_letters = []
letter_choices = list(string.ascii_lowercase)

url = "https://wordsapiv1.p.rapidapi.com/words/"

querystring = {"random": "true"}

headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': 
    }

response = requests.request("GET", url, headers=headers, params=querystring)
res = response.json()
secret_word = res['word']




def start():
    print(secret_word)
    print("Ready to play a game of hangman???")
    print("The game is simple. You have a limited number of guesses to find all the letters in a word of some length.")
    # print("You will decide the length.")
    if input("Do you wish to continue??? [Y/N] ") == "Y":
        # length = input("How long should the word be?")
        # print("I will find a " + length + " letter word for you")
        play()
    else:
        print("Guess we will play another time.\n See you later!!!")
        sys.exit()


def play():
    x = 0
    while x < 8:
        chosen = input("What letter do you want to choose?\n" + str(letter_choices) + "\n")
        chosen_letters.append(chosen)
        if str(chosen_letters[x]) in secret_word:
            print(chosen_letters[x] + " is in the word!")
            x += 1
        else:
            print("try a different letter\n")
            x += 1


start()



