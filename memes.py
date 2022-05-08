"""
Muestra un basico juego de hangman
"""
__autor__ = "TheJPMZ"
import random
import managegui as mg

status = []
guesses = []

bank = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Huckleberry", "Jackfruit", "Kiwi", "Lemon", "Mango",
        "Nectarine", "Orange", "Peach", "Pineapple", "Quince", "Raspberry", "Strawberry", "Tangerine", "Ugliberry", "Watermelon"]

word = random.choice(bank).upper()

def show_memes(status: list):
    if len(status) == 1:
        mg.draw_head()
    elif len(status) == 2:
        mg.draw_body()
    elif len(status) == 3:
        mg.draw_rifht_arm()
    elif len(status) == 4:
        mg.draw_left_arm()
    elif len(status) == 5:
        mg.draw_right_leg()
    elif len(status) == 6:
        mg.draw_left_arm()


def guess():
    x = input("Guess a letter: ").upper()
    if x in guesses:
        print("You have already guessed that letter")
        return
    if x not in word:
        status.append(x)
        guesses.append(x)
        print("Wrong")
        show_memes(status)
        return
    if x in word:
        guesses.append(x)
        print("Correct")


def menu():
    done = True

    strin = ""
    for x in word:
        if x in guesses:
            strin += " " + x
        else:
            strin += " _"
            done = False
    mg.draw_sentence(strin)

    if len(status) == 6:
        print("Has perdido")
        print("La palabra era: ", word.title())
        input("Press enter to exit")
        exit()

    if not done:
        guess()
        done = True
        menu()
        return
    else:
        print("You Won")
        input("Press enter to exit")
        exit()


def main():
    print("Welcome to the program")
    mg.init()
    while True:
        menu()


if __name__ == '__main__':
    main()
