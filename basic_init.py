import string
import sys
import requests

chosen_letters = []
wrong_guesses = []
tracker_list = []
right_guesses = []


letter_choices = list(string.ascii_lowercase)

url = "https://wordsapiv1.p.rapidapi.com/words/"

querystring = {"random": "true"}

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': "3e3e95c1b4msha49119e00fce587p15ea74jsn06eff2c680e0"
}

response = requests.request("GET", url, headers=headers, params=querystring)
res = response.json()
secret_word = res['word']

def start():
    print("Ready to play a game of hangman???")
    print("The game is simple. You have a limited number of guesses to find all the letters in a word of some length.")
    if input("Do you wish to continue??? [Y/N] ") == "Y":
        play()
    else:
        print("Guess we will play another time.\n See you later!!!")
        sys.exit()


def play():
    intro()
    print(secret_word)
    z = 0
    while z < 26:
        hangman_img()
        chosen = input("What letter do you want to choose?\n" + str(letter_choices) + "\n")
        choice_count = secret_word.count(chosen)

        x = 0
        y = 0
        while x < len(secret_word):
            if len(chosen) > 1 or chosen == '' or chosen == ' ':
                print("Try again")
                break
            elif chosen in secret_word and y < choice_count:
                letter_choices.remove(chosen)
                while y < choice_count:
                    if secret_word[x] == chosen:
                        z = secret_word.index(chosen, x, len(secret_word))
                        tracker_list.pop(z)
                        tracker_list.insert(z, chosen)
                        right_guesses.append(chosen)
                        x += 1
                        y += 1
                    else:
                        x += 1
            elif chosen in secret_word and y == choice_count:
                z = secret_word.index(chosen)
                tracker_list.pop(z)
                tracker_list.insert(z, chosen)
                right_guesses.append(chosen)
                x += 1
            else:
                print("there is none")
                wrong_guesses.append(chosen)
                x += 1
                break
        print(tracker_list)
        print("\n")
def hangman_img():
    if len(wrong_guesses) == 0:
        print("5 more guesses")
        print("....._____")
        print("....|.....O.....")
        print("....|...........")
        print("....|...........")
        print("....|...........")
        print("....|...........")
    elif len(wrong_guesses) == 1:
        print("4 more guesses")
        print("....._____")
        print("....|.....O.....")
        print("....|.....|.....")
        print("....|.....|.....")
        print("....|...........")
        print("....|...........")
    elif len(wrong_guesses) == 2:
        print("3 more guesses")
        print("....._____")
        print("....|.....O.....")
        print("....|.../.|.....")
        print("....|../..|.....")
        print("....|...........")
        print("....|...........")
    elif len(wrong_guesses) == 3:
        print("2 more guesses")
        print("....._____")
        print("....|.....O.....")
        print("....|.../.|.\...")
        print("....|../..|..\..")
        print("....|...........")
        print("....|...........")
    elif len(wrong_guesses) == 4:
        print("1 more guesses")
        print("....._____")
        print("....|.....O.....")
        print("....|.../.|.\...")
        print("....|../..|..\..")
        print("....|..../......")
        print("....|.../.......")
    elif len(wrong_guesses) == 5:
        print("0 more guesses")
        print("....._____")
        print("....|.....O.....")
        print("....|.../.|.\...")
        print("....|../..|..\..")
        print("....|..../.\....")
        print("....|.../...\...")
        print("YOU LOSE!!!")
        sys.exit()


def intro():

    space_count = secret_word.count(" ")
    for w in secret_word:
        tracker_list.append("_")
    x = 0
    y = 0
    if " " in secret_word:
        print("there are spaces in the word")
        print(space_count)

        while y < space_count:
            if secret_word[x] == ' ':
                z = secret_word.index(' ', x, len(secret_word))
                tracker_list.pop(z)
                tracker_list.insert(z, ' ')

                x += 1
                y += 1
            else:
                x += 1

        print("Your word is " + str(len(secret_word) - space_count) + " characters long!")
    else:
        print("there are no spaces")
        print("Your word is " + str(len(secret_word) - space_count) + " characters long!")




start()