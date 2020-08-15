import string
import sys
import requests

chosen_letters = []
wrong_guesses = []
letter_choices = list(string.ascii_lowercase)
# value = input("how many letter?")

url = "https://wordsapiv1.p.rapidapi.com/words/"

# https://wordsapiv1.p.mashape.com/words/?letters=6
# to get the words by length i need to change the querystring to "letters" : "some number"

# querystring = {"letters": value}
querystring = {"random": "true"}

headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key':
    }

response = requests.request("GET", url, headers=headers, params=querystring)
res = response.json()
# gives total number of words with desired letters
# ['results']['total']
# gives the words with the desired letters
# ['results']['data']
secret_word = res['word']
# secret_word = res['word']




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
        hangman_img()
        chosen = input("What letter do you want to choose?\n" + str(letter_choices) + "\n")
        chosen_letters.append(chosen)
        if str(chosen_letters[x]) in secret_word:
            print(chosen_letters[x] + " is in the word!")
            letter_choices.remove(chosen_letters[x])
            x += 1
        else:
            print("try a different letter\n")
            letter_choices.remove(chosen_letters[x])
            wrong_guesses.append(chosen)
            x += 1



def hangman_img():
    if len(wrong_guesses) == 0:
        print("5 more guesses")
    elif len(wrong_guesses) == 1:
        print("4 more guesses")
    elif len(wrong_guesses) == 2:
        print("3 more guesses")
    elif len(wrong_guesses) == 3:
        print("2 more guesses")
    elif len(wrong_guesses) == 4:
        print("1 more guesses")
    elif len(wrong_guesses) == 5:
        print("0 more guesses")
        print("YOU LOSE!!!")



start()

# hangman_img()


