import string


def start():
    print("Ready to play a game of hangman???")
    print("The game is simple. You have a limited number of guesses to find all the letters in a word of some length.")
    print("You will decide the length.")
    if input("Do you wish to continue??? [Y/N] ") == "Y" or "y":
        length = input("How long should the word be?")
        print("I will find a " + length + " letter word for you")
        play()
    else:
        print("Guess we will play another time")


def play():
    secret_word = "progress"
    chosen_letters = []
    letter_choices = list(string.ascii_lowercase)

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



