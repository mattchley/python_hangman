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
    'x-rapidapi-key': TOKEN
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
    x = 0
    while x < 26:
        # hangman_img()
        print(tracker_list)
        chosen = input("What letter do you want to choose?\n" + str(letter_choices) + "\n")
        if chosen in chosen_letters:
            print("you have used the letter already!\nTry a different letter.")
        elif chosen in secret_word:
            print(chosen + " is in the word!")
            letter_choices.remove(chosen)
            right_guesses.append(chosen)
            tracker_list.pop(secret_word.index(chosen))
            tracker_list.insert(secret_word.index(chosen), chosen)
            x += 1
        else:
            print(chosen + " is not in the word.\nTry a different letter\n")
            letter_choices.remove(chosen)
            wrong_guesses.append(chosen)
            x += 1

        chosen_letters.append(chosen)

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
    for x in secret_word:
        tracker_list.append("_")
    print("Your word is " + str(len(secret_word)) + " characters long!")
    print(tracker_list)


start()

